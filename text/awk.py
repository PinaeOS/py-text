# coding=utf-8

import os.path 
import sys 
import types

import getopt 
from getopt import GetoptError

from text import grep
from text import string_utils as str_utils

def awk(target, pattern, separator, action):
    '''
    awk : pattern scanning and text processing language
    
    @param target: string list or text file name
    @param pattern: regex pattern
    @param separator: line separator
    @param action: column index list or function: str[]=action(str[])
    
    @summary: list= ['1:huiyugeng:male', '2:zhuzhu:male']
              print awk.awk(list, '', ':', [1])
              output: ['huiyugeng', 'zhuzhu']
    
    '''
    
    text = grep.grep(target, pattern)
    if text == None:
        return None
    
    if str_utils.is_blank(separator):
        separator = ' '
    
    result = []
        
    for line in text:
        if line != None and separator in line:
            split_text = str_utils.split(line, separator)
            if action == None:
                result.append(split_text)
            elif type(action) == types.ListType:
                temp_line = []
                for column in action:
                    if str_utils.is_numeric(column):
                        temp_line.append(split_text[column])
                result.append(temp_line)
            elif type(action) == types.FunctionType:
                temp_line = action(split_text)
                if temp_line != None and type(temp_line) == types.ListType:
                    result.append(temp_line)
                
    return result

def exec_cmd(argv):
    try:
        filename = None
        pattern = None
        separator = ' '
        columns = None
        
        if len(argv) > 2:
            opts, _ = getopt.getopt(argv[2:],'hf:p:s:c:', ['help', '--file', '--pattern', '--separator', '--column'])
            for name, value in opts:
                if name in ('-h', '--help'):
                    show_help()
                if name in ('-f', '--file'):
                    filename = value
                if name in ('-p', '--pattern'):
                    pattern = value
                if name in ('-s', '--separator'):
                    separator = value
                if name in ('-c', '--column'):
                    if value != None:
                        columns = [int(c) for c in value.split(',') if str_utils.is_numeric(c.strip())]
                    
            if str_utils.is_empty(filename) or not os.path.exists(filename):
                print 'error : could not find file : ' + filename
                sys.exit()
                
            print awk(filename, pattern, separator, columns)
        else:
            show_help()
    except GetoptError, e:
        print 'error : ' + e.msg
    except Exception, e:
        print 'error : ' + e.message

def show_help():
    pass   