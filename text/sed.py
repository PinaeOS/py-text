# coding=utf-8

import types

import text_file
import grep

def sed(target, pattern, match_model, replace, operate, output):
    '''
    sed : stream editor for filtering and transforming text
    
    @param target: target: string list ,text file name or stdio
    @param pattern: regex pattern or line number pattern
    @param match_model: s: substring model, e: regex model, n: line number model
    @param replace: replacement string
    @param operate: d: delete, s: replace, a: append, i: insert
    @prarm output: : rl: return as list , rt: return as string , p: print screen, w: write to file
    
    '''
    text = text_file.read(target)
    
    result = []
    
    line_num = 1
    for line in text:

        if grep.__match(line_num, line, match_model, pattern):
            if operate == 's':
                result.append(replace)
            elif operate == 'd':
                continue
            elif operate == 'i':
                result.append(replace)
                result.append(line)
            elif operate == 'a':
                result.append(line)
                result.append(replace)
        else:
            result.append(line)
        line_num = line_num + 1
                
    output_result = '\n'.join(result)
    
    if output == 'p':
        print output_result
    elif output == 'w':
        if type(target) == types.StringType:
            text_file.write_file(target, output_result)
    elif output == 'rl':
        return text
    elif output == 'rt':
        return output_result
    
