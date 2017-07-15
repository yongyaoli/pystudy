#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 引入BIF 函数 logging
import logging
# 设置logging 的配置， 日志级别是 info
# 级别: debug info warning error
# DEBUG > INFO > WARNING > ERROR
# DEBUG 记录所有
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')

__author__ = 'Liyy'

'''
错误：
try 语句
'''

try:
    print('try...')
    r = 10 / 0
    print('result:',r)
except BaseException as e:  #所有错误类型都继承自 BaseException  
    logging.debug('出现错误:',e)
    print('BaseException:', e)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:  # except 后加上 else， else会在没有异常的时候执行
    print('no error!')
finally:  # finally 址最后必定会执行
    print('finally...')
print('END')

# 错误类型： https://docs.python.org/3/library/exceptions.html#exception-hierarchy

# 抛出自定义错误
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value:%s' % s)
    return 10 / n

foo('0')


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise   # 原样抛出捕捉到的错误信息
        # raise ZeroDivisionError('error') # 抛出时转换错误类型
        # 只要时合理的转换逻辑就可以，但是不能转换为不相干的错误，比如 IOError转ValueError

