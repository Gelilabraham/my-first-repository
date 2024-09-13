import socket
import os
import struct
import platform
import subprocess

def get_gateway_ip():
    if platform.system() == "Windows":
        result = subprocess.check_output("ipconfig", shell=True).decode()
        for line in result.split("\n"):
            if "Default Gateway" in line:
                gateway_ip = line.split(":")[-1].strip()
                return gateway_ip
    else:
        result = subprocess.check_output("ip route show", shell=True).decode()
        gateway_ip = result.split("default via ")[1].split()[0]
        return gateway_ip

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    else:
        return 'Unknown'

def ping_ip(ip):
    ping_count = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {ping_count} {ip}"
    
    response = os.system(command)
    return response == 0

def host_discovery(gateway_ip, ip_class):
    network_prefix = '.'.join(gateway_ip.split('.')[:3]) if ip_class == 'C' else '.'.join(gateway_ip.split('.')[:2])
    start_ip = 1 if ip_class == 'A' else 0
    end_ip = 254 if ip_class == 'C' else 255
    
    print(f"Scanning network: {network_prefix}.0/{8 if ip_class == 'A' else 16 if ip_class == 'B' else 24}")

    for i in range(start_ip, end_ip + 1):
        ip = f"{network_prefix}.{i}"
        if ping_ip(ip):
            print(f"Host found: {ip}")

if __name__ == "__main__":
    gateway_ip = get_gateway_ip()
    print(f"Gateway IP: {gateway_ip}")
    
    ip_class = get_ip_class(gateway_ip)
    print(f"IP Class: {ip_class}")
    
    host_discovery(gateway_ip, ip_class)
