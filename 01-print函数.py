# 使用print函数进行简单输出
a = 100
b = 200
print(111)
print(a)
print(a * b)

# 不换行一次输出多个数据
print(a, b)  # 100 200

# 使用print函数输出ASCII码对应的字符
print(chr(67))  # C
print(chr(65))  # A
print(chr(233))  # é

# 使用print函数输出中文Unicode编码
print(ord('哈'))  # 21704
print('\u5317')  # 北

# 使用print函数将内容输出到文件
fp = open('note.txt', 'w')  # 打开文件 w-->write
print('Hello Python', file=fp)  # 输出到文件中
fp.close()  # 关闭文件

# 多个print输出到一行显示
print('Hello', end='--->')
print('World')

# 使用连接符连接多个字符串
print(1, 3, 1, 4)  # 1 3 1 4
print(192, 168, 0, 0, sep='.')  # 192.168.0.0
