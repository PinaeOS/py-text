# coding=utf-8

import sys

from text import string_utils as str_utils
from text import sed, grep, awk, edit

def show_help():
    pass

def main(argv):
    sub_cmd = argv[1]
    if str_utils.is_not_empty(sub_cmd):
        if sub_cmd == 'sed':
            sed.exec_cmd(argv)
        elif sub_cmd == 'grep':
            grep.exec_cmd(argv)
        elif sub_cmd == 'awk':
            awk.exec_cmd(argv)
        elif sub_cmd == 'edit':
            edit.exec_cmd(argv)
        elif sub_cmd == 'help':
            show_help()
        else:
            show_help()

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) >= 2:
        main(argv)
    else:
        show_help() 

