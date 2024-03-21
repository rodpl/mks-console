import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.88.213', 8080))
    message = "M105"
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")
    client_socket.close()

if __name__ == "__main__":
    main()