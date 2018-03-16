"""
Part of Casper Framework
"""
from imports import *

key = 'dfslsdfdsafsalasdldsfksdfksdfkmdsf'

def encode(data):
	"""
	encode the data with the key and return the
	data to function
	"""
	obfuscated = []
	try:
		for x in range(len(data)):
			key_c = key[x % len(key)]
			enc_c = chr((ord(data[x]) + ord(key_c)) % 256)
			obfuscated.append(enc_c)
		return base64.urlsafe_b64encode("".join(obfuscated))
	except Exception as e:
		pass

def decode(data):
	"""
	decode the data with the key and return the
	data to function
	"""
	deobfuscated = []
	try:	
		data = base64.urlsafe_b64decode(data)
		for x in range(len(data)):
			key_c = key[x % len(key)]
			dec_c = chr((256 + ord(data[x]) - ord(key_c)) % 256)
			deobfuscated.append(dec_c)
		return "".join(deobfuscated)
	except Exception as e:
		pass	