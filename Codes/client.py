import socket
import json

def create_account(email, password, user_id):
    request_data = {
        'type': 'create_account',
        'email': email,
        'password': password,
        'user_id': user_id
    }
    send_request(request_data)

def sign_in(email, password):
    request_data = {
        'type': 'sign_in',
        'email': email,
        'password': password
    }
    send_request(request_data)

def send_request(request_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        s.sendall(json.dumps(request_data).encode())
        data = s.recv(1024)
        print('Received', repr(data))

# Add appropriate calls to create_account or sign_in here
# create_account('test@example.com', 'password', 'user123')
# sign_in('test@example.com', 'password')
