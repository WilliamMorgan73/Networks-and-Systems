import socket

# Define a simple password for authentication
SERVER_PASSWORD = "securepassword123"

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
        
        # Authentication step
        password = connectionSocket.recv(1024).decode()
        if password != SERVER_PASSWORD:
            print("Authentication failed.")
            connectionSocket.send("Authentication failed".encode())
            connectionSocket.close()
            continue
        else:
            print("Client authenticated successfully.")
            connectionSocket.send("Authentication successful".encode())

        # Handle multiple messages from the client after authentication
        while True:
            message = connectionSocket.recv(1024).decode()
            if not message or message.lower() == "exit":
                print("Client disconnected")
                break
            modifiedMessage = message.upper()
            connectionSocket.send(modifiedMessage.encode())

        # Close the connection with the current client
        connectionSocket.close()
        
if __name__ == "__main__":
    start_server()
