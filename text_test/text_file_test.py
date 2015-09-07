# coding=utf-8

import unittest
from text import text_file

class TextFileTest(unittest.TestCase):

    def test_read_from_http(self):
        text = text_file.read('http://www.qq.com')
        for line in text:
            print line.decode('gbk')
    
    def test_read_from_file(self):
        pass
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
