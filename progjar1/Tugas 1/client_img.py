import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.122.233', 10000)
server_address2 = ('192.168.122.117', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)
print(f"connecting to {server_address2}")
sock2.connect(server_address2)

try:
    # kirim data image
    message = open("23065-niki-zefanya.jpg", 'rb')
    message_read = message.read()
    print(f"sending {message}")
    sock.sendall(message_read)
    sock2.sendall(message_read)

    # nunggu alpine 1
    amount_received = 0
    amount_expected = len(message_read)
    file1 = bytearray()
    while amount_received < amount_expected:
        data1 = sock.recv(16)
        amount_received += len(data1)
        file1 += data1
        print("dari alpine 1: ", f"{data1}")

    # write respon dari alpine 1
    write1 = open("niki_1.jpg", 'wb')
    write1.write(file1)
    write1.close()

    # nunggu respon dari alpine 2
    amount_received2 = 0
    amount_expected2 = len(message_read)
    file2 = bytearray()
    while amount_received2 < amount_expected2:
        data2 = sock2.recv(16)
        amount_received2 += len(data2)
        file2 += data2
        print("dari alpine 2: ", f"{data2}")

    # write respon alpine 2
    write2 = open("niki_2.jpg", 'wb')
    write2.write(file2)
    write2.close()
finally:
    print("closing")
    sock.close()
    sock2.close()
