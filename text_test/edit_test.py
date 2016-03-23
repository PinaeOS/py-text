# coding=utf-8

import os
import shutil

from text import edit
from text import text_file

import unittest

class EditTest(unittest.TestCase):
    
    def test_edit(self):
        shutil.copyfile('test_file/interface_config', 'test_file/interface_config_bak')
        
        edit.edit('script_file/edit.script')
        content = text_file.read_file('test_file/interface_config_bak')
        
        self.assertTrue('iface eth0 inet static\n' in content)
        self.assertTrue('\taddress 192.168.228.31\n' in content)
        self.assertTrue('\tnetmask 255.255.255.0\n' in content)
        self.assertTrue('\tgateway 192.168.228.2\n' in content)
        self.assertTrue('iface eth1 inet dhcp\n' in content)
        
        self.assertEquals('# network interface config\n', content[0])
        self.assertEquals('# end of config\n', content[len(content) - 1])
        
        os.remove('test_file/interface_config_bak')
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
