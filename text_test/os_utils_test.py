# coding=utf-8

from text import os_utils

import unittest

class OsUtilsTest(unittest.TestCase):
    
    def test_exec_cmd(self):
        os_type = os_utils.get_os_type()
        if os_type == 'windows':
            output = os_utils.exe_cmd('ver', 'gbk', True)
        elif os_type == 'linux':
            output = os_utils.exe_cmd('uname -a', 'utf-8', True)
        for line in output:
            print line