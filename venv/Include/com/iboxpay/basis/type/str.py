# 字符串拼接，直接将两个字符串紧挨写在一起，Python会自动拼接
s1 = 'Hello,' 'World!'
print(s1)
# 上面只是一种特殊写法，并不能用于真正拼接字符串，应该用+号进行拼接
print('Hello,' + 'Kitty!')

# Python不允许直接拼接数值和字符串，程序必须先将数值转换成字符串，可以使用str()或repr()函数
print('The price is ' + str(100.0))
print('I am ' + repr(172) + ' cm tall.')

# str本身是Python内置的类型，repr()是一个函数，下面会输出带引号的字符串——字符串的Python表达式形式
print(repr("Hello World!"))

# 长字符串中可以放置任何内容，包括放置单引号、双引号，如果所定义的长字符串没有复赋值给任何变量，那么这个长字符串就被解释器忽略了
s2 = '''Let 's go fishing,said Mary.
"Ok,Let's go",said her brother.
they walked to a lake
'''
print(s2)

# python还允许使用转义字符(\)对换行符进行转义，转义之后的换行符不会中断字符串，这样可以把一个字符串写成两行
s3 = 'The quick brown fox \
   jumps over the lazy dog'
print(s3)

# 如需对Python表达式换行，同样需使用转义字符(\)进行转义
num = 20 + 3 / 4 + \
      2 * 3

# 原始字符串，原始字符串不会把反斜线当成特殊字符，例如
print(r'E:\gitRepository')
print('E:\\gitRepository')

# 如果原始字符串包含引号，程序同样需要对引号进行转义
print(r'"Let\'s go",said Charlie')

# 原始字符串结尾处如何包含反斜线，使用三引号字符串或者单写
print(r'Good Morning' '\\')

# 字节串，有多个字节组成，与字符串一一对应，bytes是不可变序列
b1 = bytes('我爱Python编程', 'UTF-8')
b2 = '学习Python很有趣'.encode('UTF-8')
b3 = b'hello'
print(b1)
print(b2)
print(b3)

# 字符串格式化，%s被称为转换说明符，指定将变量或值使用str()函数转换为字符串，%s相当于一个占位符，第二部分%作为分隔符
price = 108
print("the book's price is %s" % price)

# 如果格式化字符串中包含多个%s占位符，第三部分也应该提供多个变量
user = "liuyalou"
age = 8
print("%s is a %s year-old boy" % (user, age))

# 序列相关方法，Python字符串直接在方括号([])使用索引即可获取对应的字符，索引可为-1,0,1,2，负数代表倒数第几位
str1 = 'crazy.org is very good'
print("第一个字符为：", str1[0])
print("倒数第一个字符为：", str1[-1])
# 获取子串，不包括后一个位置指定的字符，正数从0开始，负数从1开始
print(str1[3:5])
print(str1[3:-6])
print(str1[-6:-3])
print(str1[5:])
print(str1[-6:])
# 判断字符串是否包含子串
print('very' in str1)
print('fkit' in str1)
# 获取字符串的长度，使用python内置的len()函数
print(len(str1))
print(len('test'))
# 使用全局的内置main()和max()函数获取字符串中最小字符和最大字符
print(max(str1))
print(min('abcd '))  # 空格
print(dir(str))  # 列出某个类的所有方法

# 大小写相关方法
str2 = 'out domain is crazyit.org'
print(str2.title())
print(str2.lower())
print(str2.upper())

# 删除空白，Python中的str类是不可变的，一旦形成，所包含的字符序列就不能发生任何改变
str3 = ' this is a puppy '
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())

# 查找替换相关方法
str4 = 'crazyit.org is a good site'
print(str4.startswith('crazyit'))
print(str4.endswith('site'))
print(str4.find('org'))  # 找不到不会报错，返回-1
print(str4.index('org'))
print(str4.find('org', 9))
# print(str4.index('org', 9))，使用该函数如果找不到会报错，而find函数不会
print(str4.replace('it', 'xxxx'))
print(str4.replace('it', 'xxxx', 1))  # 只替换一个
table = {97: 245, 98: 946, 116: 964}
print(str4.translate(table))  # 将字符串中指定ascii码的字符进行替换，根据翻译映射表对字符串进行查找、替换

# 使用str类的maketrans函数创建映射表
table = str.maketrans('abc', '123')
print(str4.translate(table))

# 分割、连接方法
