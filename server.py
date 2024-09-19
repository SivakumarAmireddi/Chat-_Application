import socket
import threading

# Initialize server parameters
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)  # Server listens for up to 2 clients

print(f"Server started, waiting for clients to connect...")

# Accept connections from two clients
client1, addr1 = server_socket.accept()
print(f"Connected by {addr1}")

client2, addr2 = server_socket.accept()
print(f"Connected by {addr2}")

def forward_messages(sender, receiver):
    while True:
        try:
            message = sender.recv(1024).decode('utf-8')
            if not message:
                break
            receiver.sendall(message.encode('utf-8'))
        except:
            break

# Create threads to handle forwarding messages between clients
thread1 = threading.Thread(target=forward_messages, args=(client1, client2))
thread2 = threading.Thread(target=forward_messages, args=(client2, client1))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Close connections when done
client1.close()
client2.close()
server_socket.close()
