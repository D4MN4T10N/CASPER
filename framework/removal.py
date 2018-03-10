'''
Part of Casper Framework
'''
from includes import *

payload = '''title Windows Update
ping -n 5 127.0.0.1
taskkill /IM main.exe
ping -n 5 127.0.0.1
del /q /f main.exe'''

def batch_file():
	try:
		file = open("temp.bat", "wb")
		file.write(payload)
		file.close()
		return True
	except Exception as e:
		print "[casper] Unable to create batch file > {}".format(e)

def removal():
	if (batch_file() == True):
		try:
			os.system("temp.bat")
			return True
		except Exception as e:
			print "[casper] Unable to run the batch file > {}".format(e)
	else:
		pass