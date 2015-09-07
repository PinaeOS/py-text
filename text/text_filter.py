# coding=utf-8

import sys
import types

import regex_utils
import string_utils
import grep
    
def match(text, rule_list):

    if string_utils.is_blank(text) or rule_list == None:
        return None
    
    result = []
    
    for rule_item in rule_list:
        
        match_result = {}
        result_detail = []
        
        exp_list = rule_item.get('item')
        if exp_list == None:
            continue
        
        for exp_item in exp_list:
            exp_name = exp_item.get('name').strip() if exp_item.has_key('name') else ''
            exp_type = exp_item.get('type').strip() if exp_item.has_key('type') else ''
            exp_pattern = exp_item.get('pattern').strip() if exp_item.has_key('pattern') else ''
            exp_function = exp_item.get('function').strip() if exp_item.has_key('function') else ''
            
            match_result[exp_name], result_text = __is_match(text, exp_function, exp_pattern, exp_type)
            
            # 将查询结果中不重复的部分加入匹配的详细结果中，使匹配详细结果仅保持唯一的数据
            if (result_text != None and len(result_text) > 0):
                result_detail.extend(filter(lambda line: line not in result_detail, result_text))
        
        expect = rule_item.get('expect')
        if string_utils.is_empty(expect):
            continue
        
        for key in match_result:
            expect = expect.replace(key, str(match_result.get(key)))
        try:
            rule_item['result'] = eval(expect)
            rule_item['detail'] = result_detail
        except:
            rule_item['result'] = False
            rule_item['detail'] = ''
        
        result.append(rule_item)
        
    return result

def __is_match(text, exp_function, exp_pattern, exp_type):
    result = False
    result_text = None
    
    if type(exp_function) == types.StringType:
        if regex_utils.check_line('(.*)\((.*)\)', exp_function):
            fun, value = regex_utils.parse_line('(.*)\((.*)\)', exp_function)
            
            fun = fun.strip()
            value = value.strip()
            model = 'n' if exp_type == 'line' else 'e'
    
            result_text = grep.grep(text, exp_pattern, False, model)
            if fun == 'match':
                result = result_text != None and len(result_text) > 0
            elif fun == 'count':
                if str.isdigit(value) == True:
                    count = int(value)
                    result = result_text != None and len(result_text) == count
            elif fun == 'range':
                if len(value) >= 3 and ',' in value:
                    region = value.split(',')
                    if len(region) == 2:
                        min_int, max_int = 0, sys.maxint
                        if string_utils.is_numeric(region[0]):
                            min_int = int(region[0].strip())
                        if string_utils.is_numeric(region[1]):
                            max_int = int(region[1].strip())
                        result = len(result_text) >= min_int and len(result_text) <= max_int
                        
    elif type(exp_function) == types.FunctionType:
        try:
            result, result_text = exp_function(text)
        except:
            pass
    
    return result, result_text

