# coding=utf-8

import os
import platform

from text import string_utils

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

def hostname():
    return platform.node()

def cpu():
    if os_type != 'linux':
        raise IOError('Not support ' + os_type)
    
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

def memory():
    if os_type != 'linux':
        raise IOError('Not support ' + os_type)
    
    mem_info = {}
    with open('/proc/meminfo') as f:
        for line in f:
            mem_info[line.split(':')[0]] = line.split(':')[1].strip()
    return mem_info
