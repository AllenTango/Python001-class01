import sys
import time
import socket
import threading
from queue import Queue

'''
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json
'''

# print("-" in sys.argv[6])


def iplist():
    if "-" in sys.argv[6]:
        addrs = sys.argv[6].split("-")
        addrs_list = []
        start_iplist = addrs[0].split('.')
        for i in range(int(addrs[0].split('.')[-1]), int(addrs[-1].split('.')[-1]) + 1):
            start_iplist[-1] = str(i)
            addrs_list.append('.'.join(start_iplist))
        return addrs_list


# socket.AF_INET /IPv4 socket; socket.AF_INET6 /IPv6 socket; socket.AF_UNIX /IPC(local socket)
# _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# import os
# HOST = "localhost"
# os.system('ping ' + HOST)
# PORT = 5555
_lock = threading.Lock()


def check_server(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    print(f"Attempting to connect to {address} on {port}")
    try:
        s.connect((address, port))
        with _lock:
            return f"Connected to {address} on {port}."
    except socket.error as err:
        return f"Connetion to {address} on {port} failed: {err}"
    finally:
        s.close()


def threader():
    while True:
        addr, port = q.get()
        if "-w" in sys.argv:
            with open('./' + sys.argv[-1], 'a+') as f:
                f.write('"' + str(port) + '": "' + check_server(addr, port)+ '",\n')
        check_server(addr, port)
        q.task_done()


q = Queue()

for i in range(50):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

if "ping" in sys.argv:
    for addr in iplist():
        for port in range(1,101):
            q.put((addr, port))
elif "-w" in sys.argv:
    for port in range(1,101):
        q.put((sys.argv[6], port))

q.join()
