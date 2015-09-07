# coding=utf-8

import unittest
from text import string_parser

class StringParserTest(unittest.TestCase):
    
    def test_parse_by_keyword(self):
        string = 'name test-acl src-addr 192.168.10.0 255.255.255.0 dst-addr host 192.168.199.3 service tcp 80 time-range NONE'
        resultset = string_parser.parse(string, ['name', 'src-addr', 'dst-addr', 'service', 'time-range'])
        self.assertEqual(resultset.get('name'), 'test-acl')
        self.assertEqual(resultset.get('src-addr'), '192.168.10.0 255.255.255.0')
        self.assertEqual(resultset.get('dst-addr'), 'host 192.168.199.3')
        self.assertEqual(resultset.get('service'), 'tcp 80')
        self.assertEqual(resultset.get('time-range'), 'NONE')