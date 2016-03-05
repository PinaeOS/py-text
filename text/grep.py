# coding=utf-8

import types

import text_file
import regex_utils
import string_utils

def grep(target, pattern, number = False, model = 'e'):
    '''
    grep: print lines matching a pattern
    
    @param target：string list or text file name
    @param pattern: regex pattern or line number pattern or reduce function: bool=action(str)
    @param number： with line number
    @param model： s: substring model, e: regex model, n: line number model, a: action model
    
    @summary: list= ['1:huiyugeng:male', '2:zhuzhu:male', '3:maomao:female']
              print grep.grep(list, '^(?!.*female).*$', ':', [1])
              output: ['huiyugeng', 'zhuzhu']
    '''

    if type(target) == types.StringType or type(target) == types.UnicodeType:
        text = text_file.read_file(target)
    elif type(target) == types.ListType:
        text = target
    else:
        text = None
        
    if text == None:
        return None
        
    line_num = 1;
    result = []
    
    for line_text in text:
        line_text = str(line_text)
        if __match(line_num, line_text, model, pattern):
            line_text = __print(line_num, line_text, number)
            if line_text != None:
                result.append(line_text)

        line_num = line_num + 1
    
    return result

def __match(line_num, line_text, model, pattern):
    
    if string_utils.is_blank(line_text):
        return False
    
    if string_utils.is_blank(pattern):
        return True
    
    patterns = []
    if type(pattern) == types.ListType:
        patterns = pattern
    elif type(pattern) == types.FunctionType:
        patterns = [pattern]
    else:
        patterns = [str(pattern)]
    
    if string_utils.is_empty(model) :
        model = 's'
    model = model.lower()
    
    for match_pattern in patterns:
        if model == 's':
            if match_pattern in line_text:
                return True
        elif model == 'n':
            _min, _max = __split_region(match_pattern)
            if line_num >= _min and line_num <= _max:
                return True
        elif model == 'e':
            if regex_utils.check_line(match_pattern, line_text):
                return True
        elif model == 'a':
            if type(pattern) == types.FunctionType:
                if pattern(line_text):
                    return True
            
    return False

def __split_region(pattern):
    if pattern.startswith('[') and pattern.endswith(']') and ',' in pattern:
        region = pattern[1: len(pattern) - 1].split(',')
        if region != None and len(region) == 2:
            _min = int(region[0].strip())
            _max = int(region[1].strip())
        return _min, _max
    return 0, 0

def __print(line, text, number):
    if number:
        return str(line) + ':' + text.strip()
    else:
        return text.strip()
    
