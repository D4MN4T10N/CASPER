'''
Part of Casper Framework
'''
from distutils.core import setup
import py2exe
import sys

def compile():
	try:
		entry_point = sys.argv[1]
	except Exception as e:
		sys.exit()

	sys.argv.pop()
	sys.argv.append('py2exe')
	sys.argv.append('-q')

	opts = {
		'py2exe': {
			'compressed': 2,
			'optimize': 2,
			'bundle_files': 1,
		}
	}
	setup(console=[entry_point], options=opts, zipfile=None)
	
def main():
	print '''
 >>
 >> CASPER Builder (c) rootm0s 
 >>
'''

	compile()
	
if __name__ == "__main__":
	main()