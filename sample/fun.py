#! /usr/bin/env python3
# -*- coding:utf-8 -*-

def my_abs(x):
    '''
    this is my first fun
    get the abs value
    The paramter shuld be a int
    '''
    if not isinstance(x,(int, float)):
        raise TypeError("bad operat type")
    if x>=0:
        return x
    else:
        return -x