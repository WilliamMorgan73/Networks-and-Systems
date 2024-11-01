import socket

def start_server():
    serverPort = 8080
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("localhost", serverPort))
    serverSocket.listen(1)  # Listen for incoming connections (1 client at a time)
    print("The server is ready to receive")

    while True:
        # Accept a new connection
        connectionSocket, clientAddress = serverSocket.accept()
        print(f"Connected to {clientAddress}")
        
        # Receive the message from the client
        message = connectionSocket.recv(1024).decode()
        modifiedMessage = message.upper()  # Convert the message to uppercase
        connectionSocket.send(modifiedMessage.encode())  # Send modified message back

        # Close the connection with the current client
        connectionSocket.close()
        
if __name__ == "__main__":
    start_server()