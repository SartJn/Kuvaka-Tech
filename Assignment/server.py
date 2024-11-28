import socket
import threading
import sys
#Sarthak Jain
#0901AD211051
class ChatServer:
    def __init__(self, host='127.0.0.1', port=55555):
        """
        Initialize the chat server with a host and port.
        
        Args:
            host (str): Server host IP address
            port (int): Server port number
        """
        self.host = host
        self.port = port
        
        # Store all active client connections
        self.clients = []
        
        # Create a socket server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Allow port reuse
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            # Bind the socket to the host and port
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print(f"[*] Server listening on {self.host}:{self.port}")
        except Exception as e:
            print(f"[!] Error binding server: {e}")
            sys.exit(1)
    
    def broadcast(self, message, sender_socket):
        """
        Broadcast a message to all connected clients except the sender.
        
        Args:
            message (bytes): Message to broadcast
            sender_socket (socket): Socket of the message sender
        """
        for client_socket in self.clients:
            if client_socket != sender_socket and client_socket != self.server_socket:
                try:
                    client_socket.send(message)
                except Exception as e:
                    self.remove_client(client_socket)
    
    def handle_client(self, client_socket):
        """
        Handle individual client connections.
        
        Args:
            client_socket (socket): Connected client socket
        """
        while True:
            try:
                # Receive message from client
                message = client_socket.recv(1024)
                if message:
                    print(f"[>] Received message: {message.decode('utf-8')}")
                    # Broadcast to all other clients
                    self.broadcast(message, client_socket)
                else:
                    # If no message, client likely disconnected
                    self.remove_client(client_socket)
                    break
            except Exception as e:
                self.remove_client(client_socket)
                break
    
    def remove_client(self, client_socket):
        """
        Remove a client from active connections.
        
        Args:
            client_socket (socket): Client socket to remove
        """
        if client_socket in self.clients:
            self.clients.remove(client_socket)
            client_socket.close()
    
    def start(self):
        """
        Start the chat server and accept client connections.
        """
        try:
            while True:
                # Accept incoming client connection
                client_socket, addr = self.server_socket.accept()
                print(f"[+] New connection from {addr}")
                
                # Add client to active connections
                self.clients.append(client_socket)
                
                # Start a new thread for this client
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket,)
                )
                client_thread.daemon = True
                client_thread.start()
        
        except KeyboardInterrupt:
            print("\n[*] Server shutting down...")
        finally:
            # Close all client connections
            for client_socket in self.clients:
                client_socket.close()
            self.server_socket.close()

def main():
    server = ChatServer()
    server.start()

if __name__ == "__main__":
    main()