'''
Part of Casper Framework
'''
from includes import *

def execute(cmdstr):
	try:
		logging.debug('[casper] Running command {}'.format(cmdstr))
		popen = os.popen(cmdstr)
		presult = popen.read()
		return presult
	except Exception as e:
		logging.debug('[casper] Error running command {}'.format(e))
		return False