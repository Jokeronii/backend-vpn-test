from users.protos.user_pb2 import User, UserList,Empty
from users.protos.user_pb2_grpc import UserServiceServicer
from users.models import Member

class UserService(UserServiceServicer):
    def GetUsers(self, request, context):
        members = Member.objects.all()
        users = [User(username=f"{member.firstname} {member.lastname}", email=member.email, created_at=str(member.created_at)) for member in members]
        return UserList(users=users)
