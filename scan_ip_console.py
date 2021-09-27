import argparse

from main import main

parser = argparse.ArgumentParser(description='scanner ip and port')
parser.add_argument('ip', type=str, help='ip adress')
parser.add_argument('port', help='ports')
args = parser.parse_args()

ip = args.ip
port = args.port

main(ip, port)