import socket
import threading
import subprocess
import platform

def get_available_interfaces():
    """Get available IPv4 network interfaces - short version"""
    interfaces = [("Localhost", "127.0.0.1", "Local only"), ("All interfaces", "0.0.0.0", "Any IP")]
    
    try:
        # Auto-detect OS and run appropriate command
        cmd = ['ipconfig'] if platform.system() == 'Windows' else ['ifconfig']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Parse output for IP addresses
        for line in result.stdout.split('\n'):
            if 'IPv4 Address' in line or 'inet ' in line:
                # Extract IP from Windows or Unix format
                ip = line.split(':')[1].strip().split()[0].strip('()') if ':' in line else line.split()[1].split('/')[0]
                if ip and not ip.startswith('127.') and ip not in [i[1] for i in interfaces]:
                    interfaces.append((f"Network {ip}", ip, "Detected"))
    except:
        # No fallback - if system commands fail, just use localhost and all interfaces
        pass
    
    return interfaces

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
    # Get available interfaces
    interfaces = get_available_interfaces()
    
    print("Available network interfaces:")
    print("-" * 50)
    
    for i, (name, ip, description) in enumerate(interfaces, 1):
        print(f"{i}. {name}")
        print(f"   IP: {ip}")
        print(f"   Description: {description}")
        print()
    
    while True:
        try:
            choice = int(input(f"Enter choice (1-{len(interfaces)}): "))
            if 1 <= choice <= len(interfaces):
                selected_interface = interfaces[choice - 1]
                host = selected_interface[1]
                print(f"\nSelected: {selected_interface[0]} ({host})")
                print(f"Description: {selected_interface[2]}")
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(interfaces)}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            return
    
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