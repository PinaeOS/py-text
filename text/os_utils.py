# coding=utf-8

import os
import platform

from text import string_utils

def exe_cmd(cmd, decoding = None, clean = False):
    if string_utils.is_not_empty(cmd):
        result = []
        output = os.popen(cmd).readlines()
        for line in output:
            if decoding:
                line = line.decode(decoding)
            if clean:
                line = line.strip()
            if string_utils.is_not_empty(line):
                result.append(line)
        return result
    else:
        raise ValueError('Command is Empty')
    
def get_os_type():
    return platform.system().lower()
