# coding=utf-8

from text import os_utils

import unittest

class OsUtilsTest(unittest.TestCase):
    
    def test_run(self):
        os_type = os_utils.os_type()
        if os_type == 'windows':
            output = os_utils.run('ver', 'gbk', True)
        elif os_type == 'linux':
            output = os_utils.run('uname -a', 'utf-8', True)
        for line in output:
            print line