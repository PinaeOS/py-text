# coding=utf-8

import unittest
from text import awk

class AwkTest(unittest.TestCase):

    def test_awk(self):
        resut = awk.awk('test_file/linux_df', None, None, [0,4,5])
        self.assertEqual(len(resut), 9)
        self.assertEqual(resut[1][0], '/dev/mapper/ubuntu--vg-root')
        self.assertEqual(resut[2][0], 'none')
        self.assertEqual(resut[3][0], 'udev')
        
        self.assertEqual(resut[1][1], '42%')
        self.assertEqual(resut[2][1], '0%')
        self.assertEqual(resut[3][1], '1%')
        
        self.assertEqual(resut[1][2], '/')
        self.assertEqual(resut[2][2], '/sys/fs/cgroup')
        self.assertEqual(resut[3][2], '/dev')
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
