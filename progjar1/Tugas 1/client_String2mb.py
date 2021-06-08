import sys
import socket
import random
import string

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.122.168', 10000)
server_address2 = ('192.168.122.114', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)
print(f"connecting to {server_address2}")
sock2.connect(server_address2)


try:
    # Send data
    #message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    message = ''.join(random.choices(string.ascii_lowercase, k = 2097152))
    #print(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(512)
        amount_received += len(data)
        print(f"{data}")

    # Send data
    #message2 = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    message2 = ''.join(random.choices(string.ascii_lowercase, k = 2097152))
    #print(f"sending {message2}")
    sock2.sendall(message2.encode())
    # Look for the response
    amount_received2 = 0
    amount_expected2 = len(message2)
    while amount_received2 < amount_expected2:
        data2 = sock2.recv(512)
        amount_received2 += len(data2)
        print(f"{data2}")
finally:
    print("closing")
    sock.close()
    sock2.close()
    print("closed")
