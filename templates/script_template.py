# encoding: utf-8

'''
This is what this script does.

@author: <author_name>
'''

import sys

from getopt import getopt, GetoptError

help_message = '''
usage: python <script_name.py> (<param_name>)*

e.g usage: python csv_import.py <import_path>

This is what this script does when called from shell.

options:


params:

'''

def read_nodes_csv(path,delimiter='\t'):


if __name__ == "__main__":
	'''
	This block is called when the .py file is started from the shell
	'''
	
	# checking command line options
	try:
		options, args = getopt(sys.argv[1:], "")
	except GetoptError:
		print >> sys.stderr, help_message
		sys.exit(2)
	
	# checking number of params		
	if len(args) != 1:
		print >> sys.stderr, help_message
		sys.exit(2)

	import_path = args[0]
	
	batch_import(import_path)
	#test_rel_create()

	



		
