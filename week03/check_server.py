import sys

'''
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json
'''
print(sys.argv)

import socket

# socket.AF_INET /IPv4 socket; socket.AF_INET6 /IPv6 socket; socket.AF_UNIX /IPC(local socket)
# _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 5555

def check_server(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(40)
    print(f"Attempting to connect to {address} on {port} ")
    try:
        s.connect((address, port))
        return f"Connected to {address} on {port}."
    except socket.error as err:
        return f"Connetion to {address} on {port} failed: {err} "
    finally:
        s.close()

for port in range(50, 5501,50):
    print(check_server(sys.argv[6],port))