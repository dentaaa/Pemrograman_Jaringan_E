import socket

UDP_IP_ADDRESS = '192.168.122.83'
UDP_PORT = 321

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS, UDP_PORT)))
filename = 'uussss.jpg'
fp = open(filename, 'wb+')
ditulis = 0
counter = 0
while True:
    data, addr = serverSock.recvfrom(1024)
    counter = counter+len(data)
    print(addr, counter, len(data), data)
    fp.write(data)
