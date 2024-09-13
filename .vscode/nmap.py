import nmap

def scan_ports(target_ip, ports):
    nm = nmap.PortScanner()
    nm.scan(target_ip, ports)
    
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ports = input("Enter the ports to scan: ")
    
    print(f"Scanning {target} on ports {ports}...")
    scan_ports(target, ports)