# coding=utf-8

import types
import difflib

def compare_text(src_text, dst_text):
    
    if type(src_text) == types.ListType and type(dst_text) == types.ListType:
        compare_list = diff_text(src_text, dst_text)
    
    if compare_list == None:
        compare_list = []
    
    changed_list = []
    
    for compare_item in compare_list:
        
        if compare_item.get('tag') == 'replace':
            src_item_list = compare_item.get('src_item')
            dst_item_list = compare_item.get('dst_item')
            if len(src_item_list) == len(dst_item_list):
                for i in range(len(src_item_list)):
                    changed_list.append({'src': src_item_list[i], 'dst': dst_item_list[i], 'action': 'changed'})
                    
        elif compare_item.get('tag') == 'delete':
            item_list = compare_item.get('src_item')
            for item in item_list:
                changed_list.append({'src': item, 'action': 'delete'})
                
        elif compare_item.get('tag') == 'insert':
            item_list = compare_item.get('dst_item')
            for item in item_list:
                changed_list.append({'dst': item, 'action': 'create'})
                    
    return changed_list


def stat_compare_summary(compare_list):
    summary = {}
    
    for compare_item in compare_list:
        if compare_item.has_key('action'):
            action = compare_item.get('action')
            if action in ['create', 'delete', 'changed']:
                summary[action] = summary.get(action) + 1 if summary.has_key(action) else 1
    
    return summary
 
def diff_text(src_text, dst_text, strip = False):
    
    if strip:
        src_text = [src_text.strip() for src_text in src_text]
        dst_text = [dst_text.strip() for dst_text in dst_text]
    
    seq_matcher = difflib.SequenceMatcher(None, src_text, dst_text)
    
    diff_list = []
    for tag, src_start, src_end, dst_start, dst_end in seq_matcher.get_opcodes():
        diff_result = {}
        diff_result['tag'] = tag #replace/delete/insert
        diff_result['src_start'] = src_start
        diff_result['src_end'] = src_end
        diff_result['src_item'] = src_text[src_start : src_end]
        diff_result['dst_start'] = dst_start
        diff_result['dst_end'] = dst_end
        diff_result['dst_item'] = dst_text[dst_start : dst_end]
        
        diff_list.append(diff_result)
        
    return diff_list

