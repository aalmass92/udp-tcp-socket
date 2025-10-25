import socket
import threading

class NetworkServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        
    def start_tcp_server(self):
        """Start TCP server"""
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((self.host, self.port))
        tcp_socket.listen(5)
        print(f"TCP Server listening on {self.host}:{self.port}")
        
        while True:
            client_socket, addr = tcp_socket.accept()
            print(f"TCP connection from {addr}")
            threading.Thread(target=self.handle_tcp_client, args=(client_socket,)).start()
    
    def handle_tcp_client(self, client_socket):
        """Handle TCP client connection"""
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"TCP received: {data}")
                client_socket.send(f"Echo: {data}".encode('utf-8'))
        except:
            pass
        finally:
            client_socket.close()
    
    def start_udp_server(self):
        """Start UDP server"""
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((self.host, self.port + 1))
        print(f"UDP Server listening on {self.host}:{self.port + 1}")
        
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print(f"UDP received from {addr}: {data.decode('utf-8')}")
            udp_socket.sendto(f"Echo: {data.decode('utf-8')}".encode('utf-8'), addr)

def main():
    print("Choose host interface:")
    print("1. Localhost (127.0.0.1) - Local connections only")
    print("2. All interfaces (0.0.0.0) - Accept connections from any IP")
    
    host_choice = input("Enter choice (1 or 2): ")
    
    if host_choice == '1':
        host = 'localhost'
        print("Selected: Localhost - Server will only accept local connections")
    elif host_choice == '2':
        host = '0.0.0.0'
        print("Selected: All interfaces - Server will accept connections from any IP")
    else:
        print("Invalid choice, defaulting to localhost")
        host = 'localhost'
    
    server = NetworkServer(host=host)
    
    print("\nChoose server type:")
    print("1. TCP Server")
    print("2. UDP Server")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        server.start_tcp_server()
    elif choice == '2':
        server.start_udp_server()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()