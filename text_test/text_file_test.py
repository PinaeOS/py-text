# coding=utf-8

import os
import shutil
import unittest
from text import text_file
from text.text_file import FileFilter

class TextFileTest(unittest.TestCase):
    
    def test_read_file(self):
        text = text_file.read_file('test_file/log_data')
        self.assertEqual(len(text), 19)
        
    def test_list_dir(self):
        file_filter = FileFilter(['linux.*', 'regex.*'])
        file_list = text_file.list_dir('test_file', file_filter)
        self.assertEqual(len(file_list), 6)
    
    def test_split(self):
        if os.path.exists('test_file/split') == False:
            os.mkdir('test_file/split')
        
        text_file.split('test_file/data_access', 4, 'test_file/split', 'split')
        file_list = text_file.list_dir('test_file/split')
        self.assertEqual(len(file_list), 3)
        
        shutil.rmtree('test_file/split')
        
    def test_join(self):
        file_filter = FileFilter(['log_data', 'data_access'])
        text_file.join('test_file/join.log', 'test_file', file_filter)
        size = text_file.size('test_file/join.log')
        self.assertEqual(size, 31)
        
        #os.remove('test_file/join.log')
        
    def test_size(self):
        self.assertEqual(text_file.size('test_file/log_data'), 19)
        self.assertEqual(text_file.size('test_file/data_access'), 12)
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
