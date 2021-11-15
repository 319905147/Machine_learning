# a 方式打开文件,追加内容,在文件末尾写入文件
# 注意点:不管是 a 方式打开文件,还是w 方式打开文件.写内容都是使用write()函数
f = open('3.txt', 'a', encoding='utf-8')
# 文件不存在 会创建文件
f.write('hello world\n')
f.write('hello Python\n')


f.close()




