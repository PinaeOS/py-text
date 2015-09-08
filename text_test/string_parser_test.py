# coding=utf-8

import unittest
from text import string_parser
from text import string_utils

class StringParserTest(unittest.TestCase):
    
    def test_parse_by_keyword(self):
        
        def match_line(line):
            if string_utils.is_not_empty(line):
                return len(string_utils.split(line, ';')) == 5
            return False
        
        rule_list = [
                {
                    'type' : 'regex',
                    'pattern' : 'WAF:name=(\S+); type=(\S+); protocol=(\S+); action=(\S+); message=(.*)',
                    'map' : {
                             1 : 'name',
                             2 : 'type',
                             3 : 'protocol',
                             4 : 'action',
                             5 : 'message'
                    }
                 },
                {
                    'type' : 'split',
                    'pattern' : ';',
                    'match' : match_line,
                    'map' : {
                             1 : 'date',
                             2 : 'table',
                             3 : 'category',
                             4 : 'user',
                             5 : 'ip'
                    }
                 },
                {
                    'type' : 'keyword',
                    'match' : 'startswith(rule)',
                    'map' : {
                             1 : 'name',
                             2 : 'src-addr',
                             3 : 'dst-addr',
                             4 : 'service',
                             5 : 'time-range'
                    }
                 }
            ]
        
        string = 'WAF:name=HTTP-CC; type=DDoS; protocol=tcp; action=deny; message=deny 59.61.33.121 HTTP-CC Attack'
        resultset = string_parser.parse(string, rule_list)
        self.assertEqual(resultset.get('name'), 'HTTP-CC')
        self.assertEqual(resultset.get('type'), 'DDoS')
        self.assertEqual(resultset.get('protocol'), 'tcp')
        self.assertEqual(resultset.get('action'), 'deny')
        self.assertEqual(resultset.get('message'), 'deny 59.61.33.121 HTTP-CC Attack')
        
        string = '2015-08-06;IB_BANK_TASK;Information;mofuxi;192.168.23.32'
        resultset = string_parser.parse(string, rule_list)
        self.assertEqual(resultset.get('date'), '2015-08-06')
        self.assertEqual(resultset.get('table'), 'IB_BANK_TASK')
        self.assertEqual(resultset.get('category'), 'Information')
        self.assertEqual(resultset.get('user'), 'mofuxi')
        self.assertEqual(resultset.get('ip'), '192.168.23.32')        
        
        string = 'rule name test-acl src-addr 192.168.10.0 255.255.255.0 dst-addr host 192.168.199.3 service tcp 80 time-range NONE'
        resultset = string_parser.parse(string, rule_list)
        self.assertEqual(resultset.get('name'), 'test-acl')
        self.assertEqual(resultset.get('src-addr'), '192.168.10.0 255.255.255.0')
        self.assertEqual(resultset.get('dst-addr'), 'host 192.168.199.3')
        self.assertEqual(resultset.get('service'), 'tcp 80')
        self.assertEqual(resultset.get('time-range'), 'NONE')
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()