
import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Receiver's own IP and port
ip_address = "192.168.231.133"
port_number = 5111
complete_add = (ip_address, port_number)

# Bind the socket
s.bind(complete_add)
print("Waiting for messages...")

while True:
    message, addr = s.recvfrom(1024)  # Receive data from sender
    print("Received from", addr, ":", message.decode("ascii"))
