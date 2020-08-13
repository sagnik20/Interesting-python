import socket
hostname = socket.gethostname()
IpAddress = socket.gethostbyname(hostname)

print("Your Computer name is : ", hostname)
print("Your Computer IP Address is : ", IpAddress)