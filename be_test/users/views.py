# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.conf import settings

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
        
def member_details(request,id):
    member_id = Member.objects.get(id=id)
    template = loader.get_template('member_details.html')
    context = {
        'member_id': member_id,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

class Home(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    content = {'message': 'Hello, World!'}
    return Response(content)


@api_view(['POST'])
def validate_password(request):
    username = request.data.get('username')
    password = request.data.get('password')
    secret_key = request.data.get('secret_key')

    try:
        user = get_user_model().objects.get(username=username)
    except get_user_model().DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    original_secret_key = settings.SECRET_KEY
    settings.SECRET_KEY = secret_key

    is_valid = check_password(password, user.password)

    settings.SECRET_KEY = original_secret_key

    if is_valid:
        return Response({'message': 'Password is valid'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)