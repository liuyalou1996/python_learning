print('hello world!')
# print()方法可打印多个字符串，字符串之间用逗号隔开，逗号会被当做空格处理
print('The quick brown fox', 'jumps over', 'the lazy dog')

print(300)
print(100 + 200)
print('100 + 200 =', 100 + 200)

# 可指定分隔符和结束符
print('年龄', '20', sep='|', end='\n')

# input()可获取用户输入的内容，总是返回一个字符串，Python 2.x中尽量使用raw_input()函数，相当于Python3.x中的input()
name = input('please enter you name:')

print('your name is :', name)

'''
这里面的内容都是多行注释
python语言真的很简单
'''

"""
这是用三个双引号括起来的多行注释
Python同样是允许的
"""
