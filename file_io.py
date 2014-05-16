# encoding: utf-8

''' 
file_io.py

Functions for input output with text based files files.

@author: Michael A. Huelfenhaus
'''

def read_file(filepath,encoding1, encoding2=''):
    '''
    reading files with specified encodings
    first try to use encoding1 than encoding2
    if both produce an UnicodeDecodeError the programm is terminated
    '''
    file = open(filepath,'r')
    try:
        text = unicode(file.read(),encoding1)
    except UnicodeDecodeError:
        if encoding2:
            try:
                text = unicode(file.read(),encoding2)
            except UnicodeDecodeError:
                print ("file:",filename, "has wrong coding not", encoding1, 
                       'or', encoding2)
            file.close()
			# TODO raise error
            sys.exit(3)
        else:
            print "file:",filename, "has wrong coding not", encoding1
            file.close()
			# TODO raise error
            sys.exit(3)            
    return text


def write_file(filepath,text,encoding='utf-8'):
    '''
	writing files with specified encoding
	
	default: utf-8
	'''
    file = open(filepath,'w')
    if encoding:
        file.write(text.encode(encoding))
    else:
        file.write(text)
    file.close()


def append_text_to_file(filename,text,encoding='utf-8'):
    '''
	append text to file with specified encoding
	
	default: utf-8
	'''
    file = open(filename,'a')    
    if encoding:
        file.write(text.encode(encoding))
    else:
        file.write(text)
    file.close()
