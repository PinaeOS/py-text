# coding=utf-8

import regex_utils
import string_utils
    
def parse(string, rule_list):
    
    if string_utils.is_blank(string) or rule_list == None:
        return None
    
    string = string.strip()
    
    for rule_item in rule_list:
        rule_type = rule_item.get('type').strip() if rule_item.has_key('type') else ''
        rule_type = 'regex' if rule_type == '' else rule_type
        
        pattern = rule_item.get('pattern') if rule_item.has_key('pattern') else ''
        
        if rule_type == 'regex':
            if regex_utils.check_line(pattern, string):
                value_list = regex_utils.parse_line(pattern, string)
                map_index = __build_map_index(rule_item)
                return __map_with_index(value_list, map_index)
        
        elif rule_type == 'split':
            match = rule_item.get('match') if rule_item.has_key('match') else ''
            if __is_match(match, string):
                value_list = string.split(pattern)
                map_index = __build_map_index(rule_item)
                return __map_with_index(value_list, map_index)
        
        elif rule_type == 'keyword':
            match = rule_item.get('match') if rule_item.has_key('match') else ''
            if __is_match(match, string):
                map_index = __build_map_index(rule_item)
                return __map_with_keyword(string, map_index.values())
    
    return None

def __build_map_index(rule_item):
    map_index = {}
    
    map_index_list = rule_item.get('item') if rule_item.has_key('item') else []
        
    for _map_index in map_index_list:
        try:
            if _map_index.has_key('index') and _map_index.has_key('key'):
                map_index[_map_index.get('index')] = _map_index.get('key')
        except:
            pass
    
    return map_index

def __is_match(match, line):
    result = False
    
    if regex_utils.check_line('(\S+)\((\S+)\)', match):
        fun, value = regex_utils.parse_line('(\S+)\((\S+)\)', match)
        if fun == 'startswith':
            result = line.startswith(value)
        elif fun == 'endswith':
            result = line.endswith(value)
        elif fun == 'in':
            result = value in line
    
    return result
   
def __map_with_index(value_list, map_index):
    if value_list == None or map_index == None:
        return None
    
    value_map = {}
    index = 1
    for value in value_list:
        key = map_index.get(str(index))
        if key != None:
            value_map[key] = value
        index = index + 1
        
    return value_map

def __map_with_keyword(string, keywords):
    '''
    Parse string with keywords
    
    @param string: String for parse
    @param keywords: keyword list
    
    @summary: str = 'rule service 0 protocol tcp dst-port 80 to 81'
              keywords = ['service', 'protocol', 'dst-port']
              print parse_string(str, ' ', keywords)
    
              Output: {'service':'0', 'protocol':'tcp', 'dst-port', '80 to 81'}
    '''
    value_map = {}
    
    separator = ' '
        
    key, value = None, None

    items = string.split(separator)
    for item in items:
        if string_utils.is_not_empty(item) and item.strip() in keywords:
            if value != None and key != None:
                value_map[key] = value.strip()
            key, value = item, ''
        else:
            value = value + separator + item
            
    # Add last item to resultset   
    if key != None and value != None:
        value_map[key] = value.strip()
        
    return value_map
