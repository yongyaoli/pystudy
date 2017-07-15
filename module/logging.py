#! /usr/bin/env python3
# -*- coding:utf-8 -*-


import logging


logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

#http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
