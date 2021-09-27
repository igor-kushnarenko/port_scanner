import threading
import socket


def port_scanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip, port))
        print(f'IP: {ip}, PORT: {port} - OPEN')
        sock.close()
    except:
        pass


count = 0

while count < 11:
    ip = f'192.168.0.{count}'
    for port in range(1000):
        stream = threading.Thread(target=port_scanner, args=(ip, port))
        stream.start()
    count += 1
