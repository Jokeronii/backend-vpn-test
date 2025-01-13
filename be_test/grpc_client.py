import grpc
from users.protos.user_pb2 import Empty
from users.protos.user_pb2_grpc import UserServiceStub

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = UserServiceStub(channel)
        response = stub.GetUsers(Empty())
        print("Response from server:")
        for user in response.users:
            print(f"Username: {user.username}, Email: {user.email}, Created At: {user.created_at}")

if __name__ == "__main__":
    run()
