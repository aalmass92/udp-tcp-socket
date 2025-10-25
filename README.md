# Network Communication Project

A Python-based network communication system that implements both TCP and UDP protocols for client-server communication. This project demonstrates socket programming with echo servers and configurable clients.

## 📁 Project Structure

```
data communication/
├── Server.py          # TCP/UDP Server implementation
├── client.py          # TCP/UDP Client implementation
└── README.md          # This documentation
```

## 🚀 Features

### Server Features:
- **TCP Server**: Connection-oriented, reliable communication
- **UDP Server**: Connectionless, fast communication
- **Host Selection**: Choose between localhost or all interfaces
- **Echo Functionality**: Responds with "Echo: [your message]"
- **Multithreaded**: Handles multiple TCP clients simultaneously

### Client Features:
- **Protocol Choice**: Select between TCP or UDP
- **Server Location**: Connect to localhost or remote IP
- **Port Configuration**: Use default or custom ports
- **Message Options**: Send default or custom messages
- **Real-time Feedback**: See connection status and responses

## 📋 Requirements

- Python 3.x
- No external dependencies (uses built-in `socket` and `threading` modules)

## 🛠️ Installation

1. Clone or download the project files
2. Ensure Python 3.x is installed on your system
3. No additional installation required - uses Python standard library

## 📖 Usage

### Starting the Server

1. **Run the server script:**
   ```bash
   python Server.py
   ```

2. **Choose host interface:**
   ```
   Choose host interface:
   1. Localhost (127.0.0.1) - Local connections only
   2. All interfaces (0.0.0.0) - Accept connections from any IP
   Enter choice (1 or 2): 1
   ```

3. **Select server type:**
   ```
   Choose server type:
   1. TCP Server
   2. UDP Server
   Enter choice (1 or 2): 1
   ```

4. **Server will start and display:**
   ```
   TCP Server listening on localhost:8080
   ```

### Running the Client

1. **Run the client script:**
   ```bash
   python client.py
   ```

2. **Choose client type:**
   ```
   Choose client type:
   1. TCP Client
   2. UDP Client
   Enter choice (1 or 2): 1
   ```

3. **Select server location:**
   ```
   Choose server location:
   1. Local (localhost)
   2. Remote (enter IP address)
   Enter choice (1 or 2): 1
   ```

4. **Configure port:**
   ```
   Choose TCP port:
   1. Default port (8080)
   2. Custom port
   Enter choice (1 or 2): 1
   ```

5. **Set message:**
   ```
   Choose TCP message:
   1. Default Hello message
   2. Custom message
   Enter choice (1 or 2): 2
   Enter your custom message: Hello Server!
   ```

6. **Client will connect and display:**
   ```
   Connecting to TCP server at localhost:8080
   Sending message: 'Hello Server!'
   TCP Server response: Echo: Hello Server!
   ```

## 🔧 Configuration

### Default Ports:
- **TCP Server**: 8080
- **UDP Server**: 8081

### Host Options:
- **Localhost**: `127.0.0.1` or `localhost` - Local connections only
- **All Interfaces**: `0.0.0.0` - Accept connections from any IP address



## 🖥️ Example Session

### TCP Communication:
```
Server Output:
TCP Server listening on localhost:8080
TCP connection from ('127.0.0.1', 54321)
TCP received: Hello from TCP client!

Client Output:
Connecting to TCP server at localhost:8080
Sending message: 'Hello from TCP client!'
TCP Server response: Echo: Hello from TCP client!
```

### UDP Communication:
```
Server Output:
UDP Server listening on localhost:8081
UDP received from ('127.0.0.1', 54322): Hello from UDP client!

Client Output:
Sending to UDP server at localhost:8081
Sending message: 'Hello from UDP client!'
UDP Server response: Echo: Hello from UDP client!
```

## 🔍 Code Structure

### Server.py
- `NetworkServer` class with TCP and UDP server methods
- `start_tcp_server()`: Handles TCP connections with threading
- `start_udp_server()`: Handles UDP packets
- `handle_tcp_client()`: Processes individual TCP client connections

### client.py
- `NetworkClient` class with configurable connection options
- `tcp_client()`: Establishes TCP connection and sends messages
- `udp_client()`: Sends UDP packets and receives responses
- Interactive menu system for user configuration

## 🚦 Testing

1. **Local Testing:**
   - Start server with localhost option
   - Run client with localhost option
   - Test both TCP and UDP protocols

2. **Network Testing:**
   - Start server with "all interfaces" option
   - Run client from another machine with server's IP address
   - Ensure firewall allows the configured ports

## ⚠️ Troubleshooting

### Common Issues:

1. **"Address already in use" error:**
   - Another process is using the port
   - Wait a few seconds and try again
   - Use different port numbers

2. **Connection refused:**
   - Server is not running
   - Wrong IP address or port
   - Firewall blocking connection

3. **Client can't connect to remote server:**
   - Server must be started with "all interfaces" option
   - Check firewall settings on both machines
   - Verify IP address is correct

## 📚 Learning Objectives

This project demonstrates:
- Socket programming in Python
- Deep dive on how TCP vs UDP protocol works

## 🤝Roadmap

Feel free to enhance this project by:
- Adding more protocols (WebSocket, HTTP)
- Adding encryption/security features (TLS)
- Creating a GUI interface
- Adding logging and monitoring

## 📄 License

This project is for educational purposes. Use and modify as needed for learning socket programming concepts.