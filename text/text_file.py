# coding=utf-8

import os
import types
import codecs
from text import string_utils
from text import regex_utils

def read_file(filename, encoding = 'utf-8'):
    if filename == None:
        return None
    
    text = []
    try:   
        text_file = codecs.open(filename, 'r', encoding)
        text = [line.strip() for line in text_file.readlines() if line != '']
        text_file.close()
    except IOError:
        text = None

    return text

def write_file(filename, text, encoding = 'utf-8'):
    
    try:
        text_file = codecs.open(filename, 'w', encoding)
        
        if type(text) == types.ListType:
            for line in text:
                if string_utils.is_not_empty(line):
                    text_file.write(line + '\n')
        elif type(text) == types.StringType:
            if string_utils.is_not_empty(text):
                text_file.write(text + '\n')
            
        text_file.close()
    except IOError:
        pass
    
def list_dir(dir_path, file_filter = None):
    file_list = []
    if string_utils.is_not_empty(dir_path):
        if os.path.isdir(dir_path):
            filename_list = os.listdir(dir_path)
            for filename in filename_list:
                if file_filter != None and isinstance(file_filter, FileFilter):
                    if file_filter.filter(filename):
                        file_list.append(os.path.join(dir_path, filename))
                else:
                    file_list.append(os.path.join(dir_path, filename))
    else:
        file_list = None
        
    return file_list
    
def split(filename, size, dir_path, ext_fn, encoding = 'utf-8'):
    
    name = os.path.basename(filename)
    if string_utils.is_empty(name):
        name = 'split'
    
    with codecs.open(filename, 'r', encoding) as f:
        file_counter = 1
        text = []
        for line in f:
            text.append(line)
            if len(text) >= size:
                write_file(dir_path + os.sep + name + '_' + str(file_counter) + '.' + ext_fn, text, encoding)
                text = []
                file_counter = file_counter + 1
        if len(text) > 0:
            write_file(dir_path + os.sep + name + '_' + str(file_counter) + '.' + ext_fn, text, encoding)
    pass

def join(filename, dir_path, file_filter = None, encoding = 'utf-8'):
    file_list = list_dir(dir_path, file_filter)
    
    text = []
    for file_path in file_list:
        text.extend(read_file(file_path, encoding))
        
    write_file(filename, text, encoding)

def size(filename):
    if string_utils.is_empty(filename):
        return 0
    
    size = 0
    with codecs.open(filename, 'r') as f:
        for _ in f:
            size = size + 1
    return size
            
class FileFilter(object):
    def __init__(self, file_filter):
        if file_filter != None and type(file_filter) == types.ListType:
            self.file_filter = file_filter
    
    def filter(self, filename):
        if string_utils.is_empty(filename):
            return False
        
        if hasattr(self, "file_filter"):
            flag = False
            for filter_item in self.file_filter:
                if regex_utils.check_line(str(filter_item), filename):
                    flag = True
                    break
            return flag
        else:
            return True
