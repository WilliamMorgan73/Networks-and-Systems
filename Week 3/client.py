import socket

def start_client():
    serverName = "localhost"  # or use the server IP address
    serverPort = 8080
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    clientSocket.connect((serverName, serverPort))

    message = input("Enter a message: ")
    clientSocket.send(message.encode())  # Send message to server
    modifiedMessage = clientSocket.recv(1024)  # Receive modified message from server
    print("From Server:", modifiedMessage.decode())

    clientSocket.close()  # Close the client socket
    
if __name__ == "__main__":
    start_client()
