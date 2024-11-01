import socket

def start_client():
    serverName = "localhost"  # Use "127.0.0.1" or the actual server IP if different
    serverPort = 8080
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        clientSocket.connect((serverName, serverPort))
        
        # Send client ID for authentication
        client_id = input("Enter your client ID: ")
        clientSocket.send(client_id.encode())
        
        # Receive response from server regarding client ID
        auth_response = clientSocket.recv(1024).decode()
        if auth_response != "Client ID accepted":
            print(auth_response)
            clientSocket.close()
            return  # Exit if client ID is invalid
        else:
            print("Client ID accepted. Type 'exit' to stop.")
        
        # Main messaging loop
        while True:
            message = input("Enter a message: ")
            if message.lower() == "exit":  # User chooses to stop messaging
                clientSocket.send(message.encode())  # Send exit message to server
                print("Closing connection.")
                break
            clientSocket.send(message.encode())
            server_response = clientSocket.recv(1024).decode()
            print("From Server:", server_response)

            # Check if the server response indicates a limit reached
            if "Message limit reached" in server_response:
                print("Server has restricted further messages.")
                break
            
    except Exception as e:
        print("Error connecting to server:", e)
    finally:
        clientSocket.close()
        
if __name__ == "__main__":
    start_client()
