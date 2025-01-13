import threading
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'be_test.settings')
import django
django.setup()

import grpc
from concurrent import futures
from django.core.management import execute_from_command_line
from users.protos.user_pb2_grpc import add_UserServiceServicer_to_server
from users.grpc_servicer import UserService



# func to start the gRPC server

def start_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC Server is running on port 50051")
    server.start()
    server.wait_for_termination()
    
# func to start the Django server

def start_django_server():
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])

if __name__ == "__main__":
    grpc_thread = threading.Thread(target=start_grpc_server)
    grpc_thread.start()
    start_django_server()