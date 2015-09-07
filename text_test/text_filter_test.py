# coding=utf-8

import unittest
from text import text_file
from text import text_filter

class FilterTest(unittest.TestCase):

    def test_match(self):
        
        text = text_file.read('test_file/data_access')
        
        rule_list = [
                {
                    'item': [
                                {
                                    'name' : 'date_flag',
                                    'type' : 'regex',
                                    'pattern' : '',
                                    'function' : self.date_match
                                 },
                                 {
                                    'name' : 'target_flag',
                                    'type' : 'regex',
                                    'pattern' : '192.168.23.(\d+)',
                                    'function' : 'match()'
                                 },
                                 {
                                    'name' : 'access_count',
                                    'type' : 'regex',
                                    'pattern' : '.*().*',
                                    'function' : 'range(5,)'
                                 }
                             ],
                    'expect' : 'date_flag && ip_flag && access_count'
                 }
            ]
        text_filter.match(text, rule_list)
    
    def match_date(self, text):
        return False, None
    
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
