# 1 打开文件 w 方式 打开文件 ,文件不存在会创建文件,文件存在会覆盖清空原文件
f = open('2.txt', 'w', encoding='utf-8')
# 2 写文件 文件对象.write(写入文件的内容)
f.write('hello everyone')
f.write('\n')
f.write('hello ')
f.write('你好中国')
# open函数打开文件,没有指定文件的编码,Windows下默认是gbk
# write函数将 你好中国 写入文件中,使用gbk编码写入   用gbk 方法转为二进制
# 在pycharm 中双击打开文件,默认使用的编码是utf-8
# 使用utf-8编码打开gbk会出现乱码
# 编码就是如何将中文汉字变为二进制,或者将二进制转换为汉字
# 解决方案 是两种方式的编码统一即可
#       方案一;
#       open 打开文件的时候指定utf-8打开
#
#       方案二:
#       pycharm中使用gbk的方式打开

# 3 关闭文件
f.close()











