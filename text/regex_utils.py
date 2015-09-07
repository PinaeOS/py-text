# coding=utf-8

import re

def parse_line(regex , line):
    if line == None:
        return None
    if regex == None:
        return line
    
    items = []
    pattern = re.compile(regex)
    match = pattern.match(line)
    if match:
        items = match.groups()
                
    return items

def check_line(regex, line):
    if line == None:
        return False
    if regex == None:
        return False
    pattern = re.compile(regex)
    match = pattern.match(line)
    if match:
        return True
    else:
        return False

def sub(regex, repl, line, count = 0):
    if line == None:
        return None
    if regex == None or repl == None:
        return line
    return re.sub(regex, repl, line, count)

def split(regex, line):
    if line == None:
        return None
    if regex == None:
        return line
    return re.split(regex, line)
