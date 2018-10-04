"import"
import socket
import time


"main function"
HOST, PORT = "127.0.0.1", 8787
address = (HOST,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

num = 10300

for i in range(0,num):
	client.sendto(str(i).encode(),address)
	if i%100==0:
		print("message {} sent".format(i))
	time.sleep(0.01)
client.close()

