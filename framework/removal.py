'''
Part of Casper Framework
'''
from includes import *

payload = "title Windows Update & ping -n 5 127.0.0.1 >nul & taskkill /IM  {} & ping -n 5 127.0.0.1 >nul & del /q /f {}".format(sys.argv[0],sys.argv[0])

def removal():
	try:
		popen = os.popen(payload)
		return True
	except Exception as e:
		return False