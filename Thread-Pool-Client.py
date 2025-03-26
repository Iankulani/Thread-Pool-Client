import socket

def start_client(host, port):
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")
    
    # Send a message to the server
    message = input("Enter a message to send to the server: ")
    client_socket.send(message.encode('utf-8'))

    # Receive the response from the server
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode('utf-8')}")

    # Close the connection
    client_socket.close()

# Main function to prompt user for input and start the client
def main():
    host = input("Enter the server IP address (e.g., 127.0.0.1): ")
    port = int(input("Enter the port number to connect to the server (e.g., 8080): "))
    
    start_client(host, port)

if __name__ == "__main__":
    main()
