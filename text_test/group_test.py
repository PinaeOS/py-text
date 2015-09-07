# coding=utf-8

import unittest
from text import group
import text_test

class GroupTest(unittest.TestCase):

    def test_group(self):
        linux_syslog_head = '(\S+\s+\d+)\s+(\d+:\d+:\d+)\s+(\S+)\s+'
        rule_list = [
                {
                'name' : 'auth', 
                'pattern': [linux_syslog_head + 'login\[(\d+)\].*', 
                            linux_syslog_head + 'passwd\[(\d+)\].*', 
                            linux_syslog_head + 'su\[(\d+)\].*', 
                            linux_syslog_head + 'sshd\[(\d+)\].*']
                },
                {
                'name' : 'ntp',
                'pattern' : [linux_syslog_head + 'ntpdate\[(\d+)\].*', 
                             linux_syslog_head + 'ntpd\[(\d+)\].*']
                }
            ]
        group_data = group.group(text_test.read_log(), rule_list)
        self.assertEqual(len(group_data.get('auth')), 11)
        self.assertEqual(len(group_data.get('ntp')), 4)
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
