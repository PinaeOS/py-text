# coding=utf-8

import re

def parse_line(regex , line):
    if not line:
        return None
    if not regex:
        return line
    
    items = []
    pattern = re.compile(regex)
    match = pattern.match(line)
    if match:
        items = match.groups()
                
    return items

def check_line(regex, line):
    if not line:
        return False
    if not regex:
        return False
    pattern = re.compile(regex)
    match = pattern.match(line)
    if match:
        return True
    else:
        return False
    
def match(regex, line):
    return check_line(regex, line)

def group(regex, line):
    return parse_line(regex, line)

def sub(regex, repl, line, count = 0):
    if not line:
        return None
    if not regex or not repl:
        return line
    return re.sub(regex, repl, line, count)

def split(regex, line):
    if not line:
        return None
    if not regex:
        return line
    return re.split(regex, line)
