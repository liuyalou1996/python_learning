import keyword

# 输出python中的所有关键字
print(keyword.kwlist)

# python中的字符串，字符串是以单引号或者双引号括起来的文本
print('I\'m ok')
print("I'm learning\tPython.")

# 如果字符串里面有很多字符都需要转义，就需要加很多\，r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

# 如果字符串内部有很多换行，用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

# 使用r''''''禁止字符串内部内容转义
print(r'''hello,\nworld!''')

# 布尔值，Python中一个布尔值只有True、False两种值
print(3 > 2)

# 布尔值可以用and、or和not运算
print(True and True)
print(True or False)
print(not True)

# 条件判断
age = 23
if age >= 18:
    print('adult')
else:
    print('teenager')

# 空值是Python里一个特殊的值，用None表示，None不能理解为0，因为0是有意义的，而None是一个特殊的空值
print('' == None)

# 变量，python变量本身类型不固定，因此称之为动态语言，执行a='ABC'时，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'
x = 10
x += 2
print(x)
a = 'ABC'
b = a
a = 'XYZ'
print(a, b)

# 常量，Python中通常用全部大写的变量名表示常量，事实上PI仍然是一个变量，用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359

# 除法，/除法计算结果是浮点数，即使两个整数恰好整除，结果也是浮点数，//代表地板除，两个整数的除法仍然是整数
print(10 / 3, 9 / 3, 10 // 3, 10 % 3)

# 获取数据类型
print(type(100))
print(type(100.0))
print(type('string'))
