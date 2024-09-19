import socket
import threading

# Initialize client parameters
HOST = '127.0.0.1'  # Server IP address (localhost for testing)
PORT = 12345  # Server port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Friend: {message}")
        except:
            break

def send_messages():
    while True:
        message = input("You: ")
        client_socket.sendall(message.encode('utf-8'))

# Start threads for sending and receiving messages
threading.Thread(target=receive_messages, daemon=True).start()

# Keep sending messages
send_messages()

client_socket.close()
