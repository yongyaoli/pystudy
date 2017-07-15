#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
文档测试
'''

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> dl = Dic()
    >>> dl['x'] = 100
    >>> dl.x
    100
    >>> dl.y =200
    >>> dl['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3' 
    >>> d2['empty']
    Traceback (most recent call last)
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last)
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute:%s" % key)
    
    def __setAttr__(self, key,value):
        self[key] = value

if __name__ == '__main__':
    import doctest #引入文档测试
    doctest.testmod()



