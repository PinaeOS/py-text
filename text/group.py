# coding=utf-8

import types

import regex_utils
import string_utils

def group(text, rule_list):
        
    if string_utils.is_blank(text) or rule_list == None:
        return None
        
    group_value = {}
        
    for rule_item in rule_list:
        name = rule_item.get('name') if rule_item.has_key('name') else 'NONE'
        patterns = rule_item.get('pattern') if rule_item.has_key('pattern') else []
        if type(patterns) == types.StringType:
            patterns = [patterns]
                
        for line in text:
            for pattern in patterns:
                if regex_utils.check_line(pattern, line):
                    group_items = group_value.get(name) if group_value.has_key(name) else []
                    group_items.append(line)
                    group_value[name] = group_items
        
    return group_value 

