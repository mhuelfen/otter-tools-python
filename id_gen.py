# encoding: utf-8
'''
Functions and classes to generate Ids

@author: Michael A. Huelfenhaus
'''

import os
import random 

class Id_gen(object):
    '''
	Generates Id for files and sources used combinations are saved to make
    sure the ids are unique.
	
	Only produces unique Ids if they are generated in one run.
	'''
    
    def __init__(self):
        self.combinations = []
        self.letters = "abcdefghijklmnopqrstuvwxyz" 

    def generate_id(self,path,number):
        random_part = self.new_rand_part(5)
        basename = os.path.basename(path)
        num_str = '0' * (6 - len(str(number))) + str(number)
        id = (basename[:10].lower() +  '_' * (10 - len(basename))+ '_' +
	      str(random_part) + num_str + '.txt')
        return id
    
    def generate_source_id(self,source):
        random_part = self.new_rand_part(5)
        source_id = (source[:10].lower() +  '_' * (10 - len(source))+ '_'
		     + random_part)
        return source_id
        
    def rand_letters(self,length):
        rand_str = ""
        for i in range(0, length):
            rand_str += random.sample(self.letters, 1)[0]
        return rand_str

    def new_rand_part(self,length):
        """
		generate random string of given length and make sure it was not used before"""

        random_part = self.rand_letters(length)
        while random_part in self.combinations:
            random_part = self.rand_letters(length)
        self.combinations.append(random_part)
        return random_part

def make_id(source_id,file_num,suffix):
    # remove . to avoid double points
    suffix = suffix.replace('.','')
    id = (source_id + '_' + '0' * (6 - len(str(file_num)))+ str(file_num) + '.'
	  + suffix)
    return id
    
    article_file = (article_dir + '/'+ source_id + '_' * (6 - len(str(
				    articlenr)))+ '_' + str(articlenr) + '.txt')
    new_path = (unrenamed_path+ '/'+ source_id + '_' * (10 - len(
			    file_num_suffix))+ '_' + file_num_suffix)
    

