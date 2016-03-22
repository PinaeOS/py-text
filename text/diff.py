# coding=utf-8

import difflib

def compare_text(src_text, dst_text, strip = False):
    
    src_text = src_text if src_text else []
    dst_text = dst_text if dst_text else []

    compare_list = __diff_text(src_text, dst_text, strip) \
                    if isinstance(src_text, list) and isinstance(dst_text, list) \
                    else []
    
    src_text_result = []
    dst_text_result = []
    
    line_flag = []
    line_num = 1
    
    for compare_item in compare_list:
        tag = compare_item.get('tag')
        
        src_item_list = compare_item.get('src_item')
        dst_item_list = compare_item.get('dst_item')
        
        if tag == 'equal':
            src_text_result.extend(src_item_list)
            dst_text_result.extend(dst_item_list)
            
            line_flag.append({'line' : (line_num, line_num + len(src_item_list) - 1), 'flag' : 'equal'})
            line_num = line_num + len(src_item_list)
        elif tag == 'replace':
            src_item_list = compare_item.get('src_item')
            dst_item_list = compare_item.get('dst_item')

            src_text_result.extend(src_item_list)
            dst_text_result.extend(dst_item_list)
            if len(src_item_list) > len(dst_item_list):
                dst_text_result.extend(['' for _ in range(len(src_item_list) - len(dst_item_list))])
            elif len(src_item_list) < len(dst_item_list):
                src_text_result.extend(['' for _ in range(len(dst_item_list) - len(src_item_list))])
            
            length = len(src_item_list) if len(src_item_list) > len(dst_item_list) else len(dst_item_list)
            line_flag.append({'line' : (line_num, line_num + length - 1), 'flag' : 'replace'})
            line_num = line_num + length
            
        elif tag == 'delete':
            src_text_result.extend(src_item_list)
            dst_text_result.extend(['' for _ in range(len(src_item_list))])

            line_flag.append({'line' : (line_num, line_num + len(src_item_list) - 1), 'flag' : 'delete'})
            line_num = line_num + len(src_item_list)
        elif tag == 'insert':
            src_text_result.extend(['' for _ in range(len(dst_item_list))])
            dst_text_result.extend(dst_item_list)
            
            line_flag.append({'line' : (line_num, line_num + len(dst_item_list) - 1), 'flag' : 'insert'})
            line_num = line_num + len(dst_item_list)
            
    return {'src-text' : src_text_result, 'dst-text' : dst_text_result, 'tag' : line_flag}


def stat_compare(compare_list):
    summary = {}
    
    line_tags = compare_list.get('tag')
    if line_tags != None:
        for line_tag in line_tags:
            flag = line_tag.get('flag')
            if flag and flag in ['equal', 'delete', 'insert', 'replace']:
                summary[flag] = summary.get(flag) + 1 if summary.has_key(flag) else 1
    
    return summary
 
def __diff_text(src_text, dst_text, strip = False):
    
    src_text = src_text if src_text else []
    dst_text = dst_text if dst_text else []
    
    if strip:
        src_text = [line.strip() for line in src_text]
        dst_text = [line.strip() for line in dst_text]
    
    seq_matcher = difflib.SequenceMatcher(None, src_text, dst_text)
    
    diff_list = []
    for tag, src_start, src_end, dst_start, dst_end in seq_matcher.get_opcodes():
        diff_result = {'tag' : tag,
                       'src_start' : src_start, 'src_end' : src_end,
                       'src_item' : src_text[src_start : src_end],
                       'dst_start' : dst_start, 'dst_end' : dst_end,
                       'dst_item' : dst_text[dst_start : dst_end]
                       }
        
        diff_list.append(diff_result)
        
    return diff_list

