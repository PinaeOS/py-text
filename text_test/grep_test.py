# coding=utf-8

import unittest
from text import grep
from text import string_utils
import text_test

class GrepTest(unittest.TestCase):

    def test_grep(self):
        
        log_list = text_test.read_log()
        
        linux_syslog_head = '(\S+\s+\d+)\s+(\d+:\d+:\d+)\s+(\S+)\s+'
        group_data = grep.grep(log_list, linux_syslog_head + '(login|ssh|su|sshd|passwd)\[(\d+)\].*')
        self.assertEqual(len(group_data), 11)
        
        group_data = grep.grep(log_list, '[1,4]', False, 'n')
        self.assertEqual(len(group_data), 4)
        
        group_data = grep.grep(log_list, '[1,4]', False, 'n')
        self.assertEqual(len(group_data), 4)
        
        group_data = grep.grep(log_list, 'pam', False, 's')
        self.assertEqual(len(group_data), 6)
        
        group_data = grep.grep(log_list, 'pam', True, 's')
        self.assertEqual(len(group_data), 6)
        self.assertTrue(string_utils.startswith(group_data[0], '1'))
        self.assertTrue(string_utils.startswith(group_data[1], '2'))
        self.assertTrue(string_utils.startswith(group_data[4], '12'))
        self.assertTrue(string_utils.startswith(group_data[5], '19'))
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
