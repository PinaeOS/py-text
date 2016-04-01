# coding=utf-8

import os.path 
import sys

import getopt
from getopt import GetoptError


from text import text_file
from text import grep
from text import string_utils as str_utils

def sed(target, pattern, match_model, replace, operate, output):
    '''
    sed : stream editor for filtering and transforming text
    
    @param target: target: string list ,text file name or stdio
    @param pattern: regex pattern or line number pattern
    @param match_model: s: substring model, e: regex model, n: line number model
    @param replace: replacement string
    @param operate: d: delete, s: replace, a: append, i: insert
    @prarm output: : rl: return as list , rt: return as string , p: print screen, w: write to file
    
    '''
    text = text_file.read_file(target)
    if text == None:
        return None
    
    result = []
    
    line_num = 1
    for line in text:

        if grep.__match(line_num, line, match_model, pattern):
            if operate == 's':
                if str_utils.is_not_blank(replace):
                    result.append(replace)
                else:
                    result.append(line)
            elif operate == 'd':
                continue
            elif operate == 'i':
                if str_utils.is_not_blank(replace):
                    result.append(replace)
                result.append(line)
            elif operate == 'a':
                result.append(line)
                if str_utils.is_not_blank(replace):
                    result.append(replace)
        else:
            result.append(line)
        line_num = line_num + 1
                
    output_result = ''.join(result)
    
    if output == 'p':
        print output_result
    elif output == 'w':
        if isinstance(target, str) or isinstance(target, unicode):
            text_file.write_file(target, output_result)
    elif output == 'rl':
        return result
    elif output == 'rt':
        return output_result
    
def exec_cmd(argv):
    try:
        filename = None
        pattern = None
        model = 'e'
        replace = None
        action = None
        output = 'rt'
        
        if len(argv) > 2:
            opts, _ = getopt.getopt(argv[2:],'hf:p:m:r:a:o:', ['help', '--file', '--pattern', '--model', '--replace', '--action', '--output'])
            for name, value in opts:
                if name in ('-h', '--help'):
                    show_help()
                if name in ('-f', '--file'):
                    filename = value
                if name in ('-p', '--pattern'):
                    pattern = value
                if name in ('-m', '--model'):
                    model = value
                if name in ('-r', '--replace'):
                    replace = value
                if name in ('-a', '--action'):
                    action = value
                if name in ('-o', '--output'):
                    output = value
                    
            if str_utils.is_empty(filename) or not os.path.exists(filename):
                print 'error : could not find file : ' + filename
                sys.exit()
            if str_utils.is_empty(pattern):
                print 'error : pattern is empty'
                sys.exit()
            if str_utils.is_empty(action):
                print 'error : action is Empty'
                sys.exit()
            if action in ['s', 'i', 'a'] and str_utils.is_empty(replace):
                print 'error : replace content is Empty'
                sys.exit()
                
            result = sed(filename, pattern, model, replace, action, output)
            if output == 'rt':
                print result
            elif output == 'rl':
                if result != None and isinstance(result, list):
                    print ''.join(result)
                
        else:
            show_help()
    except GetoptError, e:
        print 'error : ' + e.msg
    except Exception, e:
        print 'error : ' + e.message

def show_help():
    pass 