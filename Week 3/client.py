import socket

def start_client():
    serverName = "localhost"  # Use "127.0.0.1" or the actual server IP if different
    serverPort = 8080
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        clientSocket.connect((serverName, serverPort))
        
        # Send password for authentication
        password = input("Enter server password: ")
        clientSocket.send(password.encode())
        
        # Receive authentication response
        auth_response = clientSocket.recv(1024).decode()
        if auth_response != "Authentication successful":
            print(auth_response)
            clientSocket.close()
            return  # Exit if authentication fails
        else:
            print("Authenticated successfully. Type 'exit' to stop.")
        
        # Main messaging loop
        while True:
            message = input("Enter a message: ")
            if message.lower() == "exit":  # User chooses to stop messaging
                clientSocket.send(message.encode())  # Send exit message to server
                print("Closing connection.")
                break
            clientSocket.send(message.encode())
            modifiedMessage = clientSocket.recv(1024).decode()
            print("From Server:", modifiedMessage)
            
    except Exception as e:
        print("Error connecting to server:", e)
    finally:
        clientSocket.close()
        
if __name__ == "__main__":
    start_client()
