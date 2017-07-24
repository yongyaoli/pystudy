#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
base64
'''
import base64

r = base64.b64encode(b'my name is Liyy')
print(r)
d = base64.b64decode(r)
print(d)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

v= base64.urlsafe_b64encode(b'http://www.baidu.com/?s=z&z=z')
print(v)
e = base64.urlsafe_b64decode(v)
print(e)

b = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)
bb = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bb)

bbb = base64.urlsafe_b64decode(bb)
print(bbb)
