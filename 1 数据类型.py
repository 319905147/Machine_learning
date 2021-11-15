# import keyword  # 导包 系统中已经定义好的内容,需要使用自己导入
# print(keyword.kwlist)

# print('hello world')
result = 10
print(type(result))
# type()查看类型


name = 'Tom'
print("我的名字是%s,我很开心" % name)    # 输出字符串的格式


height = 175.22
# %f 输出小数默认保留6位
print("我的身高是%.2fcm" % height)
print('输出及格占比%d%%' % 50)    # 打印%时用两个%,即%%

print(f'我的身高是{height }')
# Python3.6版本支持使用f-string,占位统一使用{}占位,填充的数据直接写在{}里面

print('hello', end=' ')  # 可以取消换行
print('world')
# print函数默认换行  print() 相当于换行

# password = input('请输入你的密码:')
# print('你的密码为%s' % password)

weight = input('输入苹果的重量')   # input 输入的类型为字符串类型
price = input('输入苹果的单价')
result = float(price)*float(weight)     # 需要进行类型转换
# 需要进行类型转换(将原始的数据转换成我们需要的数据类型,在这个过程中不会改变原始数据,会生成一个新的数据)
print(f'苹果的重量为{weight},单价为{price}你所购买的苹果总价为{result}元')




#  转换成int类型 int(原始数据)
#  1 float类型可以转换成int
pi = 3.14
num = int(pi)
print(type(pi))  # float类型
print(type(num))    # int 类型
#  2 整数类型的字符串 "10"
my_str = '10'
num1 = int(my_str)
print(type(my_str))     # str类型
print(type(num1))   # int类型
#  3 转换float类型  float()
#  int转换成float
num2 = 14
num3 = float(num2)
print(type(num2))   # int类型
print(type(num3))   # float类型

# 将数字类型字符串转换成 float '10' '3.14'

num4 = float("10")
num5 = float('3.14')
print(type(num4))   # float 类型
print(type(num5))   # float类型

#  eval()  还原原来的数据类型,去掉字符串的引号
num6 = eval('100')  # 100 int 类型
num7 = eval('3.14')  # 3.14 float类型

num8 = eval('num7')   # num7是已经定义好的变量,未定义的变量会报错 如:num8 = eval('hello') 中hello是未定义的变量
print(type(num8))
print(type(num6))   # int类型
print(type(num7))   # float类型




height = 175.3
print(f'我的身高是{height} cm')
print(f'我的身高是{height:.2f} cm')






















