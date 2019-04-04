# Python中的字符串，在最新的Python3版本中，字符串是以Unicode进行编码的
print('包含中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr函数把编码转换为对应的字符：
# ord()函数获取字符串的十进制unicode编码，chr()函数把编码转换为对应的字符
print(ord('A'), ord('中'))
print(chr(97), chr(25991))

# b'ABC'为字节类型，每个字符只占用一个字节，含有中文的字符串无法用ascii编码，因为中文编码的范围超过了ascii编码的范围
print('ABC'.encode('ascii'), '中'.encode('utf-8'))

# 解码，将字节转换为字符串
print(b'ABC'.decode('utf-8'), b'\xe4\xb8\xad'.decode('utf-8'))
