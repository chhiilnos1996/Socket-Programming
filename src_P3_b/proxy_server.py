from socket import *
import sys

if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.

port = 8787
tcpSerSock.bind((sys.argv[1],port))
tcpSerSock.listen(5)
#############################1

# Fill in end.
while 1:

	# Strat receiving data from the client
	print('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('Received a connection from:', addr)	
	# Fill in start.		

	message = tcpCliSock.recv(2048).decode() 
	######################2
	
	# Fill in end.
	print(message)
	
	# Extract the filename from the given message
	print(message.split()[1])
	filename = message.split()[1].partition("/")[2]
	print(filename)
	fileExist = "false"
	filetouse = "/" + filename
	print(filetouse)
	
	try:
		
		# Check wether the file exist in the cache
		f = open(filetouse[1:], "r")
		outputdata = f.readlines()
		fileExist = "true"
		
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send("HTTP/1.0 200 OK\r\n")
		tcpCliSock.send("Content-Type:text/html\r\n")		
		# Fill in start.
		
		tcpCliSock.send(outputdata)
		##############################3

		# Fill in end.
		print('Read from cache')
	
	# Error handling for file not found in cache
	except IOError:
		
		if fileExist == "false":
			
			# Create a socket on the proxyserver
			 
			# Fill in start.		

			c = 
			##############################################4

			# Fill in end.
			hostn = filename.replace("www.","",1)
			print(hostn)

			try:
				
				#Connect to the socket to port 80
				# Fill in start.
				
				####################################################5

				# Fill in end.
				#
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				fileobj = c.makefile('r', 0)
				fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
				
				# Read the response into buffer
				# Fill in start.
				
				#################################################6

				# Fill in end.
				
				# Create a new file in the cache for the requested file.
				# Also send the response in the buffer to client socket and the corresponding file in the cache
				tmpFile = open("./" + filename,"wb")
				# Fill in start.

				#######################################7

				# Fill in end.
			except:
				print("Illegal request")
		else:
			# HTTP response message for file not found
			# Fill in start.
			
			#################################8

			# Fill in end.
	# Close the client and the server sockets
	tcpCliSock.close()
# Fill in start.

#####################################9

# Fill in end.
