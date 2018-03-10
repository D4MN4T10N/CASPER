'''
Part of Casper Framework
'''
from includes import *

def enable_task(task_name):
	try:
		schtasks = subprocess.Popen(['schtasks.exe','/Change','/TN',task_name,'/ENABLE'],
									stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		logging.debug("[casper] Enabled task: {}".format(task_name))
		return True
	except Exception as e:
		logging.debug("[casper] Unable to enable task: {}".format(e))
		return False

def disable_task(task_name):
	try:
		schtasks = subprocess.Popen(['schtasks.exe','/Change','/TN',task_name,'/DISABLE'],
									stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		logging.debug("[casper] Disabled task: {}".format(task_name))
		return True
	except Exception as e:
		logging.debug("[casper] Unable to disable task: {}".format(e))
		return False		

def create_task(task_name,file_name):
	try:
		schtasks = subprocess.Popen(['schtasks.exe','/Create','/SC DAILY','/TN',task_name,'/TR',file_name,'/RU SYSTEM'],
									stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		logging.debug("[casper] Created task: {}".format(task_name))
		return True		
	except Exception as e:
		logging.debug("[casper] Unable to create task: {}".format(e))
		return False

def del_task(task_name):
	try:
		schtasks = subprocess.Popen(['schtasks.exe','/Delete','/TN',task_name],
									stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		logging.debug("[casper] Deleted task: {}".format(task_name))
		return True		
	except Exception as e:
		logging.debug("[casper] Unable to delete task: {}".format(e))
		return False		

def run_task(task_name):
	try:
		schtasks = subprocess.Popen(['schtasks.exe','/Run','/TN',task_name],
									stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		logging.debug("[casper] Run task: {}".format(task_name))
		return True		
	except Exception as e:
		logging.debug("[casper] Unable to run task: {}".format(e))
		return False
