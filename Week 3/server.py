import socket

# Dictionary {client ID: message limit}
MESSAGE_LIMITS = {
    "client1": 5,
    "client2": 3,
    "client3": 7
}

# Store the count of messages sent by each client
client_message_count = {}

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
        
        # Authentication: Receive and check client ID
        client_id = connectionSocket.recv(1024).decode()
        if client_id not in MESSAGE_LIMITS:
            print("Unknown client ID.")
            connectionSocket.send("Invalid client ID".encode())
            connectionSocket.close()
            continue
        else:
            print(f"Client '{client_id}' connected with message limit {MESSAGE_LIMITS[client_id]}")
            connectionSocket.send("Client ID accepted".encode())
            client_message_count[client_id] = 0  # Initialize message count for this client

        # Handle messages from the client
        while True:
            message = connectionSocket.recv(1024).decode()
            if not message or message.lower() == "exit":
                print(f"Client '{client_id}' disconnected")
                break

            # Check if the client has reached their message limit
            if client_message_count[client_id] >= MESSAGE_LIMITS[client_id]:
                connectionSocket.send("Message limit reached. No further messages allowed.".encode())
                break
            
            # Process and send the message back
            modifiedMessage = message.upper()
            connectionSocket.send(modifiedMessage.encode())

            # Increment the client's message count
            client_message_count[client_id] += 1
            print(f"Client '{client_id}' has sent {client_message_count[client_id]} messages.")
        
        # Close the connection with the current client
        connectionSocket.close()
        
if __name__ == "__main__":
    start_server()
