# coding=utf-8

import unittest
from text import regex_utils

class RegexUtilsTest(unittest.TestCase):

    def test_check_line(self):
        self.assertTrue(regex_utils.check_line('.*(\d+.\d+.\d+.\d+)', 'MyIP is 192.168.199.4'))
        self.assertTrue(regex_utils.check_line('Test (Data|Case) For (py-text|py-task)', 'Test Data For py-text'))
        self.assertFalse(regex_utils.check_line('.*(\d+.\d+.\d+.{100,255})', 'MyIP is 192.168.199.4'))
        self.assertFalse(regex_utils.check_line(None, 'Test Word'))
        self.assertFalse(regex_utils.check_line('.*', None))
    
    def test_parse_line(self):
        result = regex_utils.parse_line('name=(\S+), type=(\S+), ip=(\S+)', 'name=ASA5505, type=Firewall, ip=192.168.199.4')
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 'ASA5505')
        self.assertEqual(result[1], 'Firewall')
        self.assertEqual(result[2], '192.168.199.4')
        
        result = regex_utils.parse_line('Test Data', None)
        self.assertEqual(result, None)
        
        result = regex_utils.parse_line(None, 'Test Data')
        self.assertEqual(result, 'Test Data')
        
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
