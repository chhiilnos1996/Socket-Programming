"import"
import socket

"class"
class myclient:

	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def connect_c(self, host, port):
		self.sock.connect((host,port))
		print("connected to "+host)
    
	def getandsend_c(self):
		print("Receive server message:")
		question = self.sock.recv(4096)
		ans = input(str(question.decode()))
		self.sock.send(ans.encode())
	
	def getend_c(self):
		print("Receive server message:")
		query = self.sock.recv(4096)
		print(str(query.decode()))
	
	def close_c(self):
		self.sock.close()
"main function"
HOST, PORT = "127.0.0.1", 8080
client = myclient()
client.connect_c(HOST,PORT)
for i in range(0,4):
	client.getandsend_c()
client.getend_c()
client.close_c()

