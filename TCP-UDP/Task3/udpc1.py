import time
import socket
#the server name and port client wishes to access
server_name = 'localhost'
server_port = 12000
#create a UDP client socket
client_port = 11000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('',client_port))

print("UDP client running...");
print("Connecting to server at IP: ", server_name, " PORT: ", server_port)

for i in range(1, 100):
    msg = str(i)

    #send the message to the udp server
    time.sleep(1.5)
    client_socket.sendto(msg.encode(),(server_name, server_port))

    #return values from the server
    msg, sadd = client_socket.recvfrom(2048)

    #show output and close client
    print(msg.decode())


client_socket.close()
