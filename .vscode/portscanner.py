import socket
def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for socket connection
        result = sock.connect_ex((target_ip, port))  # Connect to the port
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()
    
    return open_ports

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = scan_ports(target, start_port, end_port)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")