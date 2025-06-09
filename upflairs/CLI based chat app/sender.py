import socket

try:
    # Creating UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket successfully created")

    # Receiver's IP and port
    ip_address = "192.168.231.133"
    port_number = 5111
    target_add = (ip_address, port_number)

    # Get message from user
    message = input("Enter the message: ")
    encrypted_message = message.encode("ascii")

    # Send message to receiver
    s.sendto(encrypted_message, target_add)

except Exception as msg:
    print("Error:", msg)
