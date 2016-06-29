# coding=utf-8

import types

from text import text_file

class Configuration():
    def __init__(self, filename):
        self.conf = self.__load(filename)
    
    def __load(self, filename):
        conf = {}
        lines = text_file.read_file(filename)
        for line in lines:
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            else:
                try:
                    key, value = line.split('=')
                    conf[key] = value
                except:
                    pass
        return conf
    
    def save(self, filename):
        lines = []
        for key in self.conf:
            value = self.conf.get(key)
            lines.append('%s = %s', key, value)
        text_file.write_file(filename, lines)
    
    def get(self, key, default): 
        if key is not None:
            value = self.conf.get(key)
            if value is None:
                return default
                
            if type(default) == types.IntType:
                return int(value)
            elif type(default) == types.FloatType:
                return float(value)
            elif type(default) == types.BooleanType:
                return bool(value)
    
            return str(value)
            
        return None
    
    def set(self, key, value):
        if key is not None and value is not None:
            self.conf[key] = value
    