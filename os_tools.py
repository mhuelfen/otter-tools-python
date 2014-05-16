# encoding: utf-8
'''
os_file_functions.py

Functions for handlings files and paths.

@author: Michael A. Huelfenhaus
'''
import os

def list_files(source_dir):
    if os.path.isdir(source_dir):
        # list content of source directory
        dir_content = set(os.listdir(source_dir))
        file_list = [elem for elem in dir_content if os.path.isfile(
                source_dir + '/' + elem)]
    else:
        # throw exception if source_dir is no directory
        raise IOError, 'Not a directory: ' + source_dir
    return file_list
    
def list_dirs(source_dir):
    if os.path.isdir(source_dir):
        # list content of source directory
        dir_content = set(os.listdir(source_dir))
        dir_list = [elem for elem in dir_content if os.path.isdir(source_dir +
                                                                  '/' + elem)]
    else:
        # throw exception if source_dir is no directory
        raise IOError, 'Not a directory: ' + source_dir
    return dir_list
	
def list_files_ext(source_dir,exten):
    '''
	list all files in a folder with the given extension
	'''
    if os.path.isdir(source_dir):
        # list content of source directory
        dir_content = set(os.listdir(source_dir))
        # remove . from extention
        exten = exten.replace('.','')
        # changed because of 4 char endings eg html         
        file_list = [elem for elem in dir_content if os.path.isfile(
                        source_dir + '/' + elem) if elem[-(len(exten)+1):] == '.' + exten]
    else:
        # throw exception if source_dir is no directory
        raise IOError, 'Not a directory: ' + source_dir
    return file_list

def list_work_paths(source_dir):
    '''
    Returns a list of the paths with that contain the txt files
    e.g. otter/tools/1-20000
	
    MAYBE only 1 nesting
    '''
    work_paths = []
  
    # make list of source folders
    sourcefolders = list_dirs(source_dir)

    for folder in sourcefolders:
        # list folder content for subdirectory check
        dir_content = os.listdir(source_dir + '/'+ folder)
        # make list of complete subfolder paths
        subfolder_paths = [ source_dir + '/' + folder + '/' + elem  
                            for elem in dir_content if os.path.isdir(
                source_dir + '/' + folder + '/'+ elem)]

        # test if subfolders are existing
        if subfolder_paths:
            # add sub fodler to the list
            work_paths.extend(subfolder_paths)
        else:
            # if there are no sub folders add the folder to the list
            work_paths.append(source_dir + '/' + folder)

    return work_paths
    
def list_nested_work_paths(source_dir):
    '''
    Make list that contains paths for all folders of source_dir
    return a nested list of paths folders each nesting
    represents tehe content of one folder in source_dir
	
	MAYBE only 1 nesting
    '''

    # make list of source folders
    sourcefolders = list_dirs(source_dir)

    paths = []

    # fill paths list  
    for folder in sourcefolders:
        # list folder content for subdirectory check
        dir_content = os.listdir(source_dir + '/'+ folder)
        # make list of complete subfolder paths
        subfolder_paths = [ source_dir + '/' + folder + '/' + elem  
                for elem in dir_content if os.path.isdir(
                source_dir + '/' + folder + '/'+ elem)]

        # counting files in source folder for case where the structur 
    # is only 1 level deep e.g. Sources/ciao/refined/1-10000
        subfolder_file_count = len([ source_dir + '/' + folder + '/' + elem
                                     for elem in dir_content if os.path.isfile(
                    source_dir + '/' + folder + '/'+ elem)])
        
        # test if subfolders are existing and add folders to list
        if subfolder_paths:
            paths.append(subfolder_paths)
        else:
            if subfolder_file_count:
                paths.append([source_dir + '/' + folder + '/'])
    return paths


def make_nice_file_name(_string):
    '''
    Convert strings into nice filename.
    Removes all but non ascii letters and digits. Lowers string and replaces
    spaces by underscores. 
    
    @param _string: string that is converted in a nice filename
    @type _string: C{_string}
    @return: nice file name lower case and with '_' for spaces
    @rtype _string: C{_string}
    '''
    
    _string = _string.lower()                        
    # remove non alphanumeric chars except space
    _string = ''.join(ch for ch in _string if ch in valid_file_chars)
            
    _string = _string.replace(' ','_')
            
    return _string

def create_temp(target_dir):
    '''
	create a temp directory with a random element in the name
	'''
    # instaniziate Id generator
    id_generator = Id_gen()
    # Creating the path for the temporary dir with random element to make
    # sure no old temp dir is used.
    temp_dir = (os.path.dirname(os.path.abspath(target_dir)) + '/temp_' +
		id_generator.rand_letters(8))
    os.mkdir(temp_dir)    
    return temp_dir

def create_xml_file(filename,xml_declaration,dtd):
    '''
	Create a xml file and and add the xml declaration and doctype
    definition
	''' 
    file = open(filename,'w')
    file.write(xml_declaration + '\n' + dtd)
    file.close()

# def list_sources(source_dir):
#     ''''
#     Returns list of the source paths e.g. otter/tools
#     '''
#     if os.path.isdir(source_dir):
#         # list content of source directory
#         dir_content = set(os.listdir(source_dir))
#         # choose only directories
#         source_paths = [elem for elem in dir_content if os.path.isdir(
#                 source_dir + '/' + elem)]
#     else:
#         # throw exception if source_dir is no directory
#         raise IOError, 'Not a directory: ' + source_dir
#     return source_paths