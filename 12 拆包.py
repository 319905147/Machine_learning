# 组包,将多个数据值,组成元祖给到一个变量
a = 1, 2, 3
print(a)  # (1, 2, 3)


def func():
    return 1, 2  # 组包


# 拆包 , 将容器中的数据分别给到多个变量,需要注意数据的个数和变量的个数保持一致
# 注意点 容器中元祖的个数需要和变量个数保持一致

b, c, d = a  # 拆包
print(b, c, d)

e, f = func()
print(e, f)
print('*'*30)
my_list = [10, 20]
g, h = my_list
print(g, h)

print('*'*30)


my_dict = {'name': 'tom', 'age': 18}
i, j = my_dict   # key值
print(i, j)



# 交换两个变量的值
a = 10
b = 20
# 方法一
# c = a
# a = b
# b = c
# print(a, b)

# 方法二  +/-  */÷
# a = a + b   # a 30
# b = a - b   # 10
# a = a - b   # 20
# print(a, b)

# 方法三 ,Python中的使用 组包拆包
a, b = b, a
# 1 组包 (20, 10)
# 2 拆包 a, b= (20, 10)
print(a, b)







