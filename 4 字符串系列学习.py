name = 'hello world hello everyone and hello python'
print(name[len(name)-1])
print(name[1:5:3])
# 切片 格式[start:end:step]  start end 都是字符串的下标即 分别为开始和结束的下表  step是start与end之间的间隔
print(name[1:5:1])
# 字符串下标  正整数从0开始; 负整数最后一个从-1开始从后往前依次为 -1 -2 -3...

print(name[::-1])  # 将字符串倒置

print(name[:])  # 得到和原来一样的字符串

#字符串的查找
# 方法一
# find() 在字符串中查找是否存在某个字符串
# my_str.find(sub_str,start,end )
# sub_str 是在字符串中查找的内容 类型为 str  (sub_str 中带着引号     )
# start 是开始的位置 默认下标为 0
# end 是结束的位置 默认下标为 len()
# 返回值 方法执行的结果是什么 若sub_str 在字符串中 将输出其在my_str中的正数下标  ; 如果没有找到返回 -1

print(name.find('hello', 5, 36))   # 只要能找到' hello '(首次出现的) 不管是单独的还是一部分都输出其位置
print(name.find('hello', 0, 37))    # 从下标为0的位置开始找,直到下标为37的位置 找不到 返回值输出为-1

# rfind() right find() 从后边(右边)查找
print(name.rfind('everyone'))  # 从后边查找返回的是' everyone ' 第一个e的下标


# 方法二
# index() 在字符串中查找是否存在某个字符串
# my_str.index(sub_str,start,end )
# sub_str 是在字符串中查找的内容 类型为 str
# start 是开始的位置 默认下标为 0
# end 是结束的位置 默认下标为 len()
# 返回值 方法执行的结果是什么 若sub_str 在字符串中 将输出其在my_str中的正数下标  ; 如果没有找到会 报错

print(name.index('hello'))
# print(name.index('c++ java '))  # 没有找到会报错
print(name.index('python'))
# rindex() 从后边开始查找 同 rfind()

#count(sub_str,start ,end) 统计出现的次数
print(name.count('hello'))  # 3
print(name.count('c++ Java '))  # 没有找到 输出为 0 指在name这个字符串中' c++ Java ' 出现0次


#字符串的替换   replace()
# my_str.replace(old_str,new_str,count)
# 将new_str去替换_str
# count是替换的次数,默认是全部替换
# 返回值 :返回的是替换后的字符串 ,原来的字符串不变

name1 = name.replace('and', 'good', )
print('name:', name)
print('name1:', name1)
name2 = name.replace('hello', 'no good', 2)
print('name2:', name2)




#字符串的切割  split()
# my_str.split(sub_str,count)   将my_str按照sub_str进行切割
# sub_str 按照什么内容来切割 , 默认是空白字符 (空格,tab键)
# count  切割几次,默认是全部切割
# 返回值   列表[]   (其中my_str中的sub_str被切割,列表中不在有sub_str)

result = name.split()  # 按照空白字符 进行全部切割 (原字符串中的空格被切割掉,输出结果中无空格)
print(result)

print(name.split('hello', 1))    # 正面进行切割
print(name.rsplit('hello', 1))   # 从后面进行切割


#字符串的拼接 join()
# my_str.join(可迭代对象)
# 可迭代对象              str,        列表(需要列表中每一个数据都是字符串)
# 将my_str插入可迭代对象两个元素之间
# 返回值 一个新的字符串 , 不会该表原字符串的值
my_str = '_'.join('hello')  # 会把 _ 插入hello的每两个字符串之间 即 h_e_l_l_o
print(my_str)
print('*'.join('hello'))    # h*e*l*l*o

# 定义列表
my_list = ['hello', 'world', 'everyone']
print('_'.join(my_list))









