'''
Part of Casper Framework
'''
from includes import *

def hidden(value):
	try:
		window = win32console.GetConsoleWindow()
		win32gui.ShowWindow(window,value)
	except Exception as e:
		return False
	return True