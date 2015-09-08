# coding=utf-8

import unittest
from text import string_utils
from text import text_file

class StringUtilsTest(unittest.TestCase):
    
    def test_is_blank(self):
        self.assertEqual(string_utils.is_blank(None), True)
        self.assertEqual(string_utils.is_blank('word'), False)
        self.assertEqual(string_utils.is_blank(True), False)
        self.assertEqual(string_utils.is_blank(21), False)
        
    def test_is_not_blank(self):
        self.assertEqual(string_utils.is_not_blank(None), False)
        self.assertEqual(string_utils.is_not_blank('word'), True)
        self.assertEqual(string_utils.is_not_blank(True), True)
        self.assertEqual(string_utils.is_not_blank(21), True)
        
    def test_is_empty(self):
        self.assertEqual(string_utils.is_empty(None), True)
        self.assertEqual(string_utils.is_empty(' '), True)
        self.assertEqual(string_utils.is_empty('word'), False)
        self.assertEqual(string_utils.is_empty(True), False)
        self.assertEqual(string_utils.is_empty(21), False)
        
    def test_is_not_empty(self):
        self.assertEqual(string_utils.is_not_empty(None), False)
        self.assertEqual(string_utils.is_not_empty(' '), False)
        self.assertEqual(string_utils.is_not_empty('word'), True)
        self.assertEqual(string_utils.is_not_empty(True), True)
        self.assertEqual(string_utils.is_not_empty(21), True)
        
    def test_is_numeric(self):
        self.assertEqual(string_utils.is_numeric(None), False)
        self.assertEqual(string_utils.is_numeric(21), True)
        self.assertEqual(string_utils.is_numeric('21'), True)
        self.assertEqual(string_utils.is_numeric('true'), False)
        self.assertEqual(string_utils.is_numeric(True), False)
        
    def test_is_bool(self):
        self.assertEqual(string_utils.is_bool(None), False)
        self.assertEqual(string_utils.is_bool('true'), True)
        self.assertEqual(string_utils.is_bool('false'), True)
        self.assertEqual(string_utils.is_bool('True'), True)
        self.assertEqual(string_utils.is_bool('False'), True)
        self.assertEqual(string_utils.is_bool(True), True)
        self.assertEqual(string_utils.is_bool(False), True)
        self.assertEqual(string_utils.is_bool('T'), False)
        self.assertEqual(string_utils.is_bool('F'), False)

    def test_index_of(self):
        self.assertEqual(string_utils.index_of(None, 'Word'), -1)
        self.assertEqual(string_utils.index_of('Test Word', None), -1)
        self.assertEqual(string_utils.index_of('Test Word', 'Word'), 5)
        self.assertEqual(string_utils.index_of('Test Word', 'st'), 2)

    def test_index_of_any(self):
        self.assertEqual(string_utils.index_of(None, ['Word']), -1)
        self.assertEqual(string_utils.index_of('Test Word', None), -1)
        self.assertEqual(string_utils.index_of_any('Test Word', ['Word']), 5)
        self.assertEqual(string_utils.index_of_any('Test Word', ['st', 'or']), 2)

    def test_index_of_ignore_case(self):
        self.assertEqual(string_utils.index_of_ignore_case(None, 'cde'), -1)
        self.assertEqual(string_utils.index_of_ignore_case('ABCDEFG', None), -1)
        self.assertEqual(string_utils.index_of_ignore_case('ABCDEFG', 'cde'), 2)
        self.assertEqual(string_utils.index_of_ignore_case('abcdedg', 'CDE'), 2)
        self.assertEqual(string_utils.index_of_ignore_case('abcdedg', 'R'), -1)
        
    def test_last_index_of(self):
        self.assertEqual(string_utils.last_index_of(None, 'one'), -1)
        self.assertEqual(string_utils.last_index_of('one world one dream', ' '), 13)
        self.assertEqual(string_utils.last_index_of('one world one dream', 'one'), 10)
        self.assertEqual(string_utils.last_index_of('three test data', 't'), 13)
        
    def test_substring_after(self):
        self.assertEqual(string_utils.substring_after('one world one dream', 'world').strip(), 'one dream')
        self.assertEqual(string_utils.substring_after('one world one dream', 'one dream').strip(), '')
        self.assertEqual(string_utils.substring_after(None, 'one dream'), None)
        self.assertEqual(string_utils.substring_after('one world one dream', None), 'one world one dream')
        self.assertEqual(string_utils.substring_after('one world one dream', ' '), 'world one dream')
        self.assertEqual(string_utils.substring_after('one world one dream', 'Nothing'), 'one world one dream')
    
    def test_substring_after_last(self):
        self.assertEqual(string_utils.substring_after_last('one world one dream', 'world').strip(), 'one dream')
        self.assertEqual(string_utils.substring_after_last('one world one dream', 'one').strip(), 'dream')
        self.assertEqual(string_utils.substring_after_last(None, 'one dream'), None)
        self.assertEqual(string_utils.substring_after_last('one world one dream', None), 'one world one dream')
        self.assertEqual(string_utils.substring_after_last('one world one dream', ' '), 'dream')
        self.assertEqual(string_utils.substring_after_last('one world one dream', 'Nothing'), 'one world one dream')
    
    def test_substring_before(self):
        self.assertEqual(string_utils.substring_before('one world one dream', 'one').strip(), '')
        self.assertEqual(string_utils.substring_before('one world one dream', 'one dream').strip(), 'one world')
        self.assertEqual(string_utils.substring_before(None, 'one dream'), None)
        self.assertEqual(string_utils.substring_before('one world one dream', None), 'one world one dream')
        self.assertEqual(string_utils.substring_before('one world one dream', ' '), 'one')
        self.assertEqual(string_utils.substring_before('one world one dream', 'Nothing'), 'one world one dream')
        
    def test_substring_before_last(self):
        self.assertEqual(string_utils.substring_before_last('one world one dream', 'one').strip(), 'one world')
        self.assertEqual(string_utils.substring_before_last('one world one dream', 'world').strip(), 'one')
        self.assertEqual(string_utils.substring_before_last(None, 'one dream'), None)
        self.assertEqual(string_utils.substring_before_last('one world one dream', None), 'one world one dream')
        self.assertEqual(string_utils.substring_before_last('one world one dream', ' '), 'one world one')
        self.assertEqual(string_utils.substring_before_last('one world one dream', 'Nothing'), 'one world one dream')
    
    def test_substring_between(self):
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', '<tag>', '</tag>'), 'Hello')
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', '<tag>', '</div>'), 'Hello</tag>')
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', '<div>', '</tag>'), '<tag>Hello')
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', '<div>', '</div>'), '<tag>Hello</tag>')
        self.assertEqual(string_utils.substring_between(None, '<div>', '</div>'), None)
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', '<tag>', None), 'Hello</tag>')
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', None, '</tag>'), '<tag>Hello')
        self.assertEqual(string_utils.substring_between('<tag>Hello</tag>', None, None), '<tag>Hello</tag>')
    
    
    def test_left(self):
        self.assertEqual(string_utils.left(None, 3), None)
        self.assertEqual(string_utils.left('abcdefg', 0), '')
        self.assertEqual(string_utils.left('abcdefg', 3), 'abc')
        self.assertEqual(string_utils.left('abcdefg', 4), 'abcd')
        self.assertEqual(string_utils.left('abcdefg', 5), 'abcde')
        self.assertEqual(string_utils.left('abcdefg', 8), 'abcdefg')

    def test_right(self):
        self.assertEqual(string_utils.right(None, 3), None)
        self.assertEqual(string_utils.right('abcdefg', 0), '')
        self.assertEqual(string_utils.right('abcdefg', 3), 'efg')
        self.assertEqual(string_utils.right('abcdefg', 4), 'defg')
        self.assertEqual(string_utils.right('abcdefg', 5), 'cdefg')
        self.assertEqual(string_utils.right('abcdefg', 8), 'abcdefg')
    
    def test_mid(self):
        self.assertEqual(string_utils.mid(None, 3, 3), None)
        self.assertEqual(string_utils.mid('abcdefg', 3, 3), 'def')
        self.assertEqual(string_utils.mid('abcdefg', 4, 3), 'efg')
        self.assertEqual(string_utils.mid('abcdefg', 5, 3), 'fg')
        self.assertEqual(string_utils.mid('abcdefg', 2, 3), 'cde')
        self.assertEqual(string_utils.mid('abcdefg', 8, 3), 'abcdefg')
        
    def test_left_pad(self):
        self.assertEqual(string_utils.left_pad('abc', 3, '*'), '***abc')
        self.assertEqual(string_utils.left_pad('abc', 3), '***abc')
        self.assertEqual(string_utils.left_pad('abc', 3, '.'), '...abc')
    
    def test_right_pad(self):
        self.assertEqual(string_utils.right_pad('abc', 3, '*'), 'abc***')
        self.assertEqual(string_utils.right_pad('abc', 3), 'abc***')
        self.assertEqual(string_utils.right_pad('abc', 3, '.'), 'abc...')
    
    def test_abbreviate(self):
        self.assertEqual(string_utils.abbreviate('abcdef', 3, 3), 'abc***')
        self.assertEqual(string_utils.abbreviate('abcdef', 2, 3), 'ab***')
        self.assertEqual(string_utils.abbreviate('abcdef', 6, 3), 'abcdef')
        self.assertEqual(string_utils.abbreviate('abcdef', 3, 0), 'abc')
        self.assertEqual(string_utils.abbreviate('abcdef', 3, 3, '.'), 'abc...')
        
    def test_repeat(self):
        self.assertEqual(string_utils.repeat('*', 3), '***')
        self.assertEqual(string_utils.repeat(None, 3), '***')
        
    def test_count_matches(self):
        self.assertEqual(string_utils.count_matches(None, ' '), 0)
        self.assertEqual(string_utils.count_matches('   ', None), 0)
        self.assertEqual(string_utils.count_matches('   ', ' '), 3)
        self.assertEqual(string_utils.count_matches('one world one dream', 'one'), 2)
        self.assertEqual(string_utils.count_matches('three test data for terminal tree', 't'), 6)
    
    def test_remove_start(self):
        self.assertEqual(string_utils.remove_start('one world one dream', 'one').strip(), 'world one dream')
        self.assertEqual(string_utils.remove_start('one world one dream', 'Nothing').strip(), 'one world one dream')
        self.assertEqual(string_utils.remove_start('one world one dream', None).strip(), 'one world one dream')
        self.assertEqual(string_utils.remove_start(None, 'Nothing'), None)
        
    def test_remove_end(self):
        self.assertEqual(string_utils.remove_end('one world one dream', 'one').strip(), 'one world  dream')
        self.assertEqual(string_utils.remove_end('one world one dream', 'Nothing').strip(), 'one world one dream')
        self.assertEqual(string_utils.remove_end('one world one dream', None).strip(), 'one world one dream')
        self.assertEqual(string_utils.remove_end(None, 'Nothing'), None)
        
    def test_split(self):
        split_list = string_utils.split('data   test    world', ' ')
        self.assertEqual(len(split_list), 3)
        self.assertEqual(split_list[0], 'data')
        self.assertEqual(split_list[1], 'test')
        self.assertEqual(split_list[2], 'world')
        
        split_list = string_utils.split('data ; test ; world', ';')
        self.assertEqual(len(split_list), 3)
        self.assertEqual(split_list[0], 'data')
        self.assertEqual(split_list[1], 'test')
        self.assertEqual(split_list[2], 'world')
        
    def test_strip_all(self):
        strings = [' ', ' one world', 'one dream ', None, 21]
        result = string_utils.strip_all(strings)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], '')
        self.assertEqual(result[1], 'one world')
        self.assertEqual(result[2], 'one dream')
        self.assertEqual(result[3], None)
        self.assertEqual(result[4], '21')
        
    def test_contains_any(self):
        self.assertEqual(string_utils.contains_any('one world one dream', 'one'), True)
        self.assertEqual(string_utils.contains_any('one world one dream', ['one']), True)
        self.assertEqual(string_utils.contains_any('one world one dream', ['world', 'dream']), True)
        self.assertEqual(string_utils.contains_any(None, ['world', 'dream']), False)
        self.assertEqual(string_utils.contains_any('Test Data For py_text', ['world', 'dream']), False)
    
    def test_contains(self):
        self.assertEqual(string_utils.contains('one world one dream', 'one'), True)
        self.assertEqual(string_utils.contains(None, 'one'), False)
        self.assertEqual(string_utils.contains('one world one dream', None), False)
        
    def test_to_string(self):
        self.assertEqual(string_utils.to_string(None), None)
        self.assertEqual(string_utils.to_string(21), '21')
        self.assertEqual(string_utils.to_string(True), 'True')
        self.assertEqual(string_utils.to_string('one world one dream'), 'one world one dream')
        
    def test_replace_all(self):
        self.assertEqual(string_utils.replace_all(None, 'one', 'One'), None)
        self.assertEqual(string_utils.replace_all('one world one dream', 'one', 'One'), 'One world One dream')
        self.assertEqual(string_utils.replace_all('one world one dream', None, 'One'), 'one world one dream')
        self.assertEqual(string_utils.replace_all('one world one dream', 'one', None), 'one world one dream')
    
    def test_replace_each(self):
        self.assertEqual(string_utils.replace_each(None, ['one'], ['One']), None)
        self.assertEqual(string_utils.replace_each('one world one dream', ['one', 'world', 'dream'], ['One', 'World', 'Dream']), 'One World One Dream')
        self.assertEqual(string_utils.replace_each('one world one dream', [None, 'world', 'dream'], ['One', 'World', 'Dream']), 'one World one Dream')
        self.assertEqual(string_utils.replace_each('one world one dream', None, None), 'one world one dream')
        
    def test_match(self):
        
        text = text_file.read('test_file/data_access')
        
        def match_date(text):
            
            result = []
            for line in text:
                items = string_utils.split(line, ';')
                if items != None and len(items) == 5:
                    date = items[0]
                    _, _, day = date.split('-')
                    if int(day) >= 1 and int(day) <=15:
                        result.append(line)
            
            if len(result) > 0:
                return result
            else:
                return None
        
        rule_list = [match_date, '.*192.168.23.(\d+).*', '.*(OM_WF_RECEPTION_WAITING|IB_WL_BINDDEALRES).*']
        result = string_utils.text_filter(text, rule_list)
        
        self.assertEqual(len(result), 4)   

if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    