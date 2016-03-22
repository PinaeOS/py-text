# coding=utf-8

import unittest
from text import diff
from text import text_file

class DiffTest(unittest.TestCase):
    
    def test_compare_text(self):
        diff_text_src = text_file.read_file('test_file/diff_text_src')
        diff_text_dst = text_file.read_file('test_file/diff_text_dst')
        
        compare_result = diff.compare_text(diff_text_src, diff_text_dst)
        summary = diff.stat_compare(compare_result)
        self.assertEqual(summary.get('equal'), 3)
        self.assertEqual(summary.get('delete'), 1)
        self.assertEqual(summary.get('insert'), 1)
        self.assertEqual(summary.get('replace'), 1)
        
        src_text = compare_result.get('src-text')
        dst_text = compare_result.get('dst-text')
        self.assertEqual(len(src_text), 9)
        self.assertEqual(len(dst_text), 9)
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
