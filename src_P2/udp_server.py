"import"
import socket
import time


"main function"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST, PORT = "127.0.0.1", 8787
server.bind((HOST,PORT))
count = 0 
num = 10000
print("UDP server is ready")

while(True):
	data,addr = server.recvfrom(64)
	data = int(data.decode())
	
	if data>=num:
		print("{} :break".format(data))
		break
	else:
		count = count+1

server.close()
print("{}/{} were received".format(count,num))



	
