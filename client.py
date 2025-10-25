import socket

# Client code for TCP and UDP communication
class NetworkClient:
    # User input or default port variables
    def __init__(self, tcp_port=8080, udp_port=8081):
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        
        # Get server host and port from user
    def get_server_host(self):
        """Get server host from user choice"""
        print("\nChoose server location:")
        print("1. Local (localhost)")
        print("2. Remote (enter IP address)")
        
        host_choice = input("Enter choice (1 or 2): ")
        
        if host_choice == '1':
            return 'localhost'
        elif host_choice == '2':
            ip_address = input("Enter server IP address: ")
            return ip_address
        else:
            print("Invalid choice, defaulting to localhost")
            return 'localhost'

    # Get server port from user choice
    def get_server_port(self, protocol):
        """Get server port from user choice"""
        default_port = self.tcp_port if protocol == 'TCP' else self.udp_port
        
        print(f"\nChoose {protocol} port:")
        print(f"1. Default port ({default_port})")
        print("2. Custom port")
        
        port_choice = input("Enter choice (1 or 2): ")
        
        if port_choice == '1':
            return default_port
        elif port_choice == '2':
            try:
                custom_port = int(input(f"Enter {protocol} port number: "))
                if 1 <= custom_port <= 65535:
                    return custom_port
                else:
                    print("Invalid port range (1-65535), using default")
                    return default_port
            except ValueError:
                print("Invalid port number, using default")
                return default_port
        else:
            print("Invalid choice, using default port")
            return default_port

    def get_message(self, protocol):
        """Get message from user choice"""
        print(f"\nChoose {protocol} message:")
        print("1. Default Hello message")
        print("2. Custom message")
        
        message_choice = input("Enter choice (1 or 2): ")
        
        if message_choice == '1':
            return f"Hello from {protocol} client!"
        elif message_choice == '2':
            custom_message = input("Enter your custom message: ")
            return custom_message if custom_message.strip() else f"Hello from {protocol} client!"
        else:
            print("Invalid choice, using default message")
            return f"Hello from {protocol} client!"

    # TCP client connection
    def tcp_client(self, server_host, server_port, message):
        """TCP client connection"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            print(f"Connecting to TCP server at {server_host}:{server_port}")
            client_socket.connect((server_host, server_port))
            
            # Send data
            print(f"Sending message: '{message}'")
            client_socket.send(message.encode('utf-8'))
            
            # Receive response
            response = client_socket.recv(1024)
            print(f"TCP Server response: {response.decode('utf-8')}")
            
        except Exception as e:
            print(f"TCP Error: {e}")
        finally:
            client_socket.close()

    def udp_client(self, server_host, server_port, message):
        """UDP client connection"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            server_address = (server_host, server_port)
            
            print(f"Sending to UDP server at {server_host}:{server_port}")
            
            # Send data
            print(f"Sending message: '{message}'")
            client_socket.sendto(message.encode('utf-8'), server_address)
            
            # Receive response
            response, server = client_socket.recvfrom(1024)
            print(f"UDP Server response: {response.decode('utf-8')}")
            
        except Exception as e:
            print(f"UDP Error: {e}")
        finally:
            client_socket.close()
    #
    def start_client(self):
        """Main client interface"""
        print("Choose client type:")
        print("1. TCP Client")
        print("2. UDP Client")
        
        choice = input("Enter choice (1 or 2): ")
        
        # Get server host
        server_host = self.get_server_host()
        
        if choice == '1':
            server_port = self.get_server_port('TCP')
            message = self.get_message('TCP')
            self.tcp_client(server_host, server_port, message)
        elif choice == '2':
            server_port = self.get_server_port('UDP')
            message = self.get_message('UDP')
            self.udp_client(server_host, server_port, message)
        else:
            print("Invalid choice")

def main():
    client = NetworkClient()
    client.start_client()

if __name__ == "__main__":
    main()