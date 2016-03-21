# coding=utf-8

import os.path
import sys

import getopt
from getopt import GetoptError

import text_file
import regex_utils
import string_utils as str_utils

def __read_script(script, encoding = 'utf8'):
    file_reg = '\[(.*)\]'
    cmd_reg = '(\w+)\s*:\s*(.*)'
    
    tag_file = None
    cmd_set = {}
    
    if isinstance(script, str):
        content = text_file.read_file(script, 'all', encoding, True)
    elif isinstance(script, list):
        content = script
    elif isinstance(script, dict):
        return script
    else:
        raise IOError('script must be a filename or script command list')
    
    for line in content:
        if str_utils.is_empty(line):
            continue
        line = line.strip()
        if str_utils.startswith(line, '#'):
            continue
        if regex_utils.check_line(file_reg, line):
            tag_file = regex_utils.parse_line(file_reg, line)[0]
            if str_utils.is_not_empty(tag_file):
                tag_file = tag_file.strip()
        elif regex_utils.check_line(cmd_reg, line):
            cmd_item = regex_utils.parse_line(cmd_reg, line)
            if tag_file is not None and cmd_item is not None and len(cmd_item) == 2:
                cmd_list = cmd_set.get(tag_file) if cmd_set.has_key(tag_file) else []
                cmd_list.append(cmd_item)
                cmd_set[tag_file] = cmd_list
                
    return cmd_set

def __parse_line_num(cmd_arg, content):
    line_nums = []
    
    if cmd_arg.startswith('/') and cmd_arg.endswith('/'):
        line_items = cmd_arg[1 : len(cmd_arg) - 1].split(',')
        for line_item in line_items:
            line_item = line_item.strip()
            if '-' in line_item:
                line_min, line_max = line_item.split('-')
                if line_max > line_min:
                    line_nums.extend([i - 1 for i in range(int(line_min), int(line_max) + 1)])
            else:
                if str_utils.is_numeric(line_item):
                    line_nums.append(int(line_item) - 1)
    elif cmd_arg == '[:end]':
        line_nums.append(len(content))
    elif cmd_arg == '[:start]':
        line_nums.append(0)
    else:
        line_counter = 0
        for line in content:
            try:
                if regex_utils.check_line(cmd_arg, line):
                    line_nums.append(line_counter)
            except Exception,e:
                print e
            line_counter += 1
                
    result = []
    for line_num in line_nums:
        if line_num not in result:
            result.append(line_num)
            
    return result
        
def __delete(cmd_arg, content):
    line_nums = __parse_line_num(cmd_arg, content)
    for line_num in line_nums:
        if line_num <= len(content):
            content[line_num] = None
    return content

def __update(cmd_arg, content):
    line_nums, value = __split_arg(cmd_arg, content)
    for line_num in line_nums:
        if line_num <= len(content):
            value = __reduce_value(value)
            content[line_num] = value
    return content

def __add(cmd_arg, content):
    line_nums, value = __split_arg(cmd_arg, content)
    for line_num in line_nums:
        value = __reduce_value(value)
        content.insert(line_num + 1, value)
    return content

def __create(filename):
    parent_dir = os.path.dirname(filename)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    open(filename, 'w').close()

def __reduce_value(value):
    if value != None:
        value = value.replace('[:ht]', '\t')
        value = value.replace('[:lf]', '\n')
        value = value.replace('[:cr]', '\r')
        if not value.endswith('\n'):
            value = value + '\n'
    return value

def __split_arg(cmd_arg, content):
    idx_arg = str_utils.index_of(cmd_arg, '->')
    line_nums = __parse_line_num(cmd_arg[:idx_arg], content)
    value = cmd_arg[idx_arg + 2 :]
    return line_nums, value

def edit(script, base_path = None, encoding = 'utf8', output = 'w'):
    cmd_set = __read_script(script)
    for filename in cmd_set:
        if str_utils.is_empty(filename):
            continue
        cmd_list = cmd_set.get(filename)
        if str_utils.is_not_empty(base_path):
            if filename.startswith('/'):
                filename = base_path + filename
            else:
                filename = os.path.join(base_path, filename)
        if os.path.exists(filename):
            if os.path.isdir(filename):
                continue
        else:
            __create(filename)
        content = text_file.read_file(filename, 'all', encoding, False)
        for cmd_item in cmd_list:
            cmd = cmd_item[0].strip()
            cmd_arg = cmd_item[1].strip()
            if str_utils.is_not_empty(cmd):
                cmd = cmd.lower()
                if cmd == 'd':
                    content = __delete(cmd_arg, content)
                elif cmd == 'u':
                    content = __update(cmd_arg, content)
                elif cmd == 'a':
                    content = __add(cmd_arg, content)
                elif cmd == 'c':
                    content = []
                        
        content = [line for line in content if line != None]
        if output == 'w':
            text_file.write_file(filename, content, encoding, '')
        else:
            print ''.join(content)

   
def exec_cmd(argv):
    try:
        script = None
        encoding = 'utf8'
        output = 'w'
        
        if len(argv) > 2:
            opts, _ = getopt.getopt(argv[2:], 'hs:e:o:', ['help', '--script', '--encoding', '--output'])
            for name, value in opts:
                if name in ('-h', '--help'):
                    show_help()
                if name in ('-s', '--script'):
                    script = value
                if name in ('-e', '--encoding'):
                    encoding = value
                if name in ('-o', '--output'):
                    output = value
                    
            if str_utils.is_empty(script) or not os.path.exists(script):
                print 'error : could not find script file : ' + script
                sys.exit()
            edit(script, encoding, output)
        else:
            show_help()
    except GetoptError, e:
        print 'error : ' + e.msg
    except Exception, e:
        print 'error : ' + e.message

def show_help():
    pass
