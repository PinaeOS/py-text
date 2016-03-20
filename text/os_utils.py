# coding=utf-8

import os
import platform

from text import string_utils

def check_os(os_list):
    def decorators(func):
        def wrapper(*args, **kwargs):
            os_t = os_type()
            if os_t not in os_list:
                    raise ValueError('Not Support :' + os_t)
            return func( *args , **kwargs)
        return wrapper
    return decorators

def run(cmd, decoding = None, clean = False):
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
    
def os_type():
    return platform.system().lower()

@check_os(['linux'])
def cpu():    
    nprocs = 0
    cpu_info = {}
    proc_info = {}
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                #end of one processor
                cpu_info['proc%s' % nprocs] = proc_info
                nprocs = nprocs + 1
                #Reset
                proc_info = {}
            else:
                if len(line.split(':')) == 2:
                    proc_info[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    proc_info[line.split(':')[0].strip()] = ''
    return cpu_info

@check_os(['linux'])
def memory():
    mem_info = {}
    with open('/proc/meminfo') as f:
        for line in f:
            mem_info[line.split(':')[0]] = line.split(':')[1].strip()
    return mem_info


