import socket

for port in range(0,500):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("10.0.0.206", port))
    if result == 0:
        print("Port "   + str(port) +   " is open")
    else:
        print("Port "   + str(port) +   " is closed")
    sock.close()