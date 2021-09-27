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


def get_range_ip():
    ip_list = []
    user_input = input()
    res = user_input.split('/')
    user_ip = res[0][:-1]
    start_ip = int(res[0].split('.')[-1])
    end_ip = int(res[1])
    for ip in range(start_ip, end_ip):
        ip_list.append(f'{user_ip}{ip}')
    return ip_list


def main():
    ip_list = get_range_ip()
    port_list = [80, 25, 100, 333]
    for ip in ip_list:
        for port in range(1000):
            stream = threading.Thread(target=port_scanner, args=(ip, port))
            stream.start()


if __name__ == '__main__':
    main()
