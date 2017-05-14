#! /usr/bin/env python3
# -* coding: utf-8 -*-

"""
第二天
数据类型; 变量；字符串；编码
"""

print("python 对大小写敏感.")
print("python类型：整形,使用十六进制表示整数,以0x开头，以0-9,a-z 表示")
print(0xff00)
print(0xa5b4c3d2)
print("浮点型，也就是小数")
print(1.23e9)
print(1.23e8)
print(1.2e-5)
print("字符串就是以'或者\"包括起来的任意文本,注意转义")
print('I\'m \"OK\"!')
print('转义字符\\可以转义很多字符，比如\\n表示换行，\\t表示制表符，字符\\本身也要转义，所以\\\表示的字符就是\\')
print('I\'m learning\nPython.')
print('\\\n\\')

print('如果字符串内部有很多字符都需要转义，可以采用r''表示''内的字符串默认都不转义')
print('\\\t\\')
print(r'\\\t\\')
print("如果内容有很多换行，可以采用三个单引号")
print('''测试一下
haha 
没有问题啊''')
print("布尔类型，即True,False, 或者通过布尔运算计算出来")
b = False
print(b)
print(2>1)
print(True and False)
print(False or True)
print(True and True)
print(False and False)

print(not True)

print("python 中的空值用None表示，意思是没有\n")
print("python中变量名必须是大小写英文，数字，'_'组合而成, 不能使用数字开头")

age = 1
print(age)
name = "T1000"
print(name)

print("常量：python中采用大写字母表示常量")

print("python第一种除法是/: 10/4")
print(10/4)
print("第二种除法是//,成为地板除,两个整数相除结果是整数: 10//4")
print(10//4)
print("% 是求余运算: 10%4:")
print(10%4)

print("Python对bytes类型的数据用带b前缀的单引号或双引号表示")
print(b'ABC')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('中文A'))
#print('中文'.encode('ascii'))  这句报错,报错的原因是因为 中文不能用ascii码表示


print("""
#! /usr/bin/env python3
# -* coding: utf-8 -*-
""")
print("第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释")
print("第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码")

print("----"*10+"\n")
print("字符的格式化:%s 字符串, %d 数字, %f 浮点, %x 十六进制")

print("Hi, i am %s"%'zhang')
print('Hi,%s,I am %d years old, I have %f money, test: %x'%('zhangsan',19,88.50,0xff00))


print('测试小数补0: %2d===%03d'%(3,1))

print("测试浮点数截取:%f,截取小数点后三位%.3f"%(3.14159261111111,3.1415926))

print("当不知道参数是什么类型的时候  就可以直接使用%s\n如果字符串里%是普通字符想输出% 就要使用两个%")
print("test %d %%"%7)
print("\n 作业:")
print("小明去年%d,今年%d,提高了%d, 提高了%.1f%%"%(72,85,85-72,(85-72)/72*100))
