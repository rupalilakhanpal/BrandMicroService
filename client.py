import socket

# Define host and port
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Get brand name input from the user
brand_name = input("Enter brand name: ")

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    
    # Send the brand name to the server
    s.sendall(brand_name.encode('utf-8'))
    
    # Receive and print the response from the server
    response = s.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")