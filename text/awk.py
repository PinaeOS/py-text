# coding=utf-8

import types

import grep
import string_utils

def awk(target, pattern, separator, action):
    '''
    awk : pattern scanning and text processing language
    
    @param target: string list or text file name
    @param pattern: regex pattern
    @param separator: line separator
    @param action: column index list or function
    
    @summary: list= ['1:huiyugeng:male', '2:zhuzhu:male']
              print awk.awk(list, '', ':', [1])
              output: ['huiyugeng', 'zhuzhu']
    
    '''
    
    if string_utils.is_blank(separator):
        separator = ' '
    
    text = grep.grep(target, pattern)
    
    result = []
        
    for line in text:
        if line != None and separator in line:
            split_text = string_utils.split(line, separator)
            if action == None:
                result.append(split_text)
            elif type(action) == types.ListType:
                temp_line = []
                for column in action:
                    if string_utils.is_numeric(column):
                        temp_line.append(split_text[column])
                result.append(temp_line)
            elif type(action) == types.FunctionType:
                temp_line = action(temp_line)
                if temp_line != None and type(temp_line) == types.ListType:
                    result.append(temp_line)
                
    return result
    