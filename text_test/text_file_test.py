# coding=utf-8

import unittest
from text import text_file

class TextFileTest(unittest.TestCase):

    def test_read_from_http(self):
        text = text_file.read('https://raw.githubusercontent.com/interhui/py-text/master/text_test/test_file/log_data')
        self.assertEqual(len(text), 19)
    
    def test_read_from_file(self):
        text = text_file.read('test_file/log_data')
        self.assertEqual(len(text), 19)
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
