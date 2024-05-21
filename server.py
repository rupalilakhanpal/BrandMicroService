import socket

# Define host and port
HOST = '127.0.0.1'  # Loopback address
PORT = 65432        # Port to listen on

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    
    # Listen for incoming connections
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    
    # Accept a connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            
            # Process the received data
            brand_name = data.decode('utf-8').strip()
            print(f"Received brand name: {brand_name}")
            
            # Check if the brand is on the boycott list
            boycott_list = ["Brand1", "Brand2", "Brand3"]
            if brand_name in boycott_list:
                result = "Boycott"
            else:
                result = "Not on boycott list"
            
            # Send the result back to the client
            conn.sendall(result.encode('utf-8'))