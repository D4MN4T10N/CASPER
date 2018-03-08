'''
Part of Casper Framework

This is stolen cuz why not KEK
'''
from includes import *

key = 'Very long and confidential key LULZ'

def encode(data):
	obfuscated = []
	for x in range(len(data)):
		key_c = key[x % len(key)]
		enc_c = chr((ord(data[x]) + ord(key_c)) % 256)
		obfuscated.append(enc_c)
	return base64.urlsafe_b64encode("".join(obfuscated))

def decode(data):
	deobfuscated = []
	data = base64.urlsafe_b64decode(data)
	for x in range(len(data)):
		key_c = key[x % len(key)]
		dec_c = chr((256 + ord(data[x]) - ord(key_c)) % 256)
		deobfuscated.append(dec_c)
	return "".join(deobfuscated)
