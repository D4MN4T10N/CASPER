"""
Part of Casper Framework
"""
from imports import *

def hidden(value):
	"""
	get the console window and hide it
	"""
	try:
		GetConsoleWindow = win32console.GetConsoleWindow()
		win32gui.ShowWindow(GetConsoleWindow,value)
		return True
	except Exception as e:
		return False