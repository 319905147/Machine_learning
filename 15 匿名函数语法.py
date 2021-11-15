# 使用 lambda 关键字定义的函数就是匿名函数
"""
1.匿名函数中不能使用 if 语句 ,while 循环 ,for 循环,只能编写单行的表达式,或函数调用,普通函数都可以
2.匿名函数中的赶回结果不需要使用return , 表达式的运行结果就是返回结果,普通函数返回结果必须使用return
3. 匿名函数中也可以不返回结果,例如 :lambda:print('hello world')
""" 

# lambda 参数列表 : 表达式

# 1 五参数无返回值
def 函数名():
    函数代码

lambda: 函数代码


# 2 无参数有返回值
def 函数名():
    return 1+2

lambda : 1+2  # 唯一一个有冒号 不换行


# 3 有参数无返回值
def 函数名():
    print(a, b)

lambda a, b: print(a, b)


# 4 有参数有返回值
def 函数名():
    return a + b


lambda a, b: a+b





























