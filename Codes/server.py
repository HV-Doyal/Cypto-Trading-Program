import socket
import threading
import json

def handle_client(conn):
    data = conn.recv(1024).decode()
    request_data = json.loads(data)

    if 'type' not in request_data:
        conn.sendall(b'Invalid request')
        return

    if request_data['type'] == 'create_account':
        email = request_data['email']
        password = request_data['password']
        user_id = request_data['user_id']
        try:
            with open('user_data.txt', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if email in users:
            conn.sendall(b'Account already exists.')
        else:
            users[email] = {'password': password, 'user_id': user_id}
            with open('user_data.txt', 'w') as file:
                json.dump(users, file)
            conn.sendall(b'Account created successfully!')

    elif request_data['type'] == 'sign_in':
        email = request_data['email']
        password = request_data['password']
        try:
            with open('user_data.txt', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if email in users and users[email]['password'] == password:
            conn.sendall(b'Sign in successful!')
        else:
            conn.sendall(b'Invalid username or password.')
    else:
        conn.sendall(b'Invalid request type')

    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()


if __name__ == "__main__":
    start_server()
