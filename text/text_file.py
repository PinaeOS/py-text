# coding=utf-8

import os
import types
import urllib
from text import string_utils

def read(target):
    
    if target == None:
        return None
    
    target_type = type(target)
    text = []
    if target_type == types.ListType or target_type == types.FunctionType:
        text = target
    elif target_type == types.StringType:

        if target.startswith('http'):
            try:
                web_url = urllib.urlopen(target)
                text = [line.strip() for line in web_url.readlines() if line != '']
                web_url.close()
            except IOError:
                text = None
        else:
            try:   
                text_file = open(target, 'r')
                text = [line.strip() for line in text_file.readlines() if line != '']
                text_file.close()
            except IOError:
                text = None

    return text


def read_files(filename_list):
    
    text = []
    
    if type(filename_list) == types.ListType:
        for filename in filename_list:
            text.extend(read(filename))
    
    return text

def write_file(filename, text, encoding = 'utf-8'):
    #TODO write file with encoding
    try:
        text_file = open(filename, 'w')
        
        if type(text) == types.ListType:
            for line in text:
                text_file.write(line)
        elif type(text) == types.StringType:
            text_file.write(text)
            
        text_file.close()
    except IOError:
        pass
    
def split(filename, size, path, ext_fn, encoding = 'utf-8'):
    
    name = os.path.basename(filename)
    if string_utils.is_empty(name):
        name = 'split'
    
    with open(filename, 'r') as f:
        file_counter = 1
        text = []
        for line in f:
            text.append(line)
            if len(text) >= size:
                write_file(path + os.sep + name + '_' + str(file_counter) + '.' + ext_fn, text, encoding)
                text = []
                file_counter = file_counter + 1
        if len(text) > 0:
            write_file(path + os.sep + name + '_' + str(file_counter) + '.' + ext_fn, text, encoding)
    pass

def join(filename, dir_path):
    pass

def read_property(filename, comment=False):
    config = {}
    try:
        _file = open(filename , 'r')
        comment = ''
        for line in _file.readlines():
            line = line.strip()
            if line.startswith('#') == False and line != '':
                key, value = line.split('=')
                if comment :
                    config[key] = {}
                    config[key]['value'] = value.strip()
                    if comment != '':
                        config[key]['comment'] = comment
                        comment = ''
                else:
                    config[key] = value.strip()
            else:
                comment = line[1:len(line)]
        _file.close()
    except IOError:
        config = None
    return config


def write_property(filename, config):
    try:
        _file = open(filename, 'w')
        for key in config.keys():
            _config_item = config.get(key)
            if isinstance(_config_item, dict):
                if _config_item.has_key('comment'):
                    _file.write('#{0}\n'.format(_config_item.get('comment')))
                if _config_item.has_key('value'):
                    _file.write('{0}={1}\n'.format(key, _config_item.get('value')))
            else:
                _file.write('{0}={1}\n'.format(key, _config_item))
        _file.close()
    except IOError:
        pass
