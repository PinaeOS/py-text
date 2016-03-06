# coding=utf-8

import unittest
from text import sed
from text import grep

class SedTest(unittest.TestCase):

    def test_sed(self):
        result = sed.sed('test_file/sshd_config', '#ListenAddress 0.0.0.0', 'e', 'ListenAddress 192.168.228.123', 's', 'rl')
        self.assertEqual(len(grep.grep(result, '.*(192.168.228.123).*')), 1)
        
        self.assertEqual(len(grep.grep(result, 'PrintMotd no')), 1)
        result = sed.sed('test_file/sshd_config', 'PrintMotd no', 'e', '', 'd', 'rl')
        self.assertEqual(len(grep.grep(result, 'PrintMotd no')), 0)
         
        self.assertEqual(len(grep.grep(result, 'UseLogin yes')), 0)
        result = sed.sed('test_file/sshd_config', 'TCPKeepAlive yes', 'e', 'UseLogin yes', 'a', 'rl')
        self.assertEqual(len(grep.grep(result, 'UseLogin yes')), 1)
        
        self.assertEqual(len(grep.grep(result, 'Banner /opt/ssh_banner')), 0)
        result = sed.sed('test_file/sshd_config', '#Banner /etc/issue.net', 'e', 'Banner /opt/ssh_banner', 'i', 'rl')
        self.assertEqual(len(grep.grep(result, 'Banner /opt/ssh_banner')), 1)
        
        result = sed.sed('test_file/sshd_config', None, 'e', 'Something', 'i', 'rl')
        
        result = sed.sed('test_file/sshd_config', '#Banner /etc/issue.net', 'e', None, 'i', 'rl')
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
