# 在函数中定义的局部变量,或者通过计算得出的局部变量,想要在函数外部访问和使用,此时就可以使用return 关键字,将这个返回值返回
# return 关键字作用:
# 1 将return 后边的数据值进行返回
# 2 程序代码遇到return 会终止(结束)执行
# 注意点 return 关键字必须写在函数中

def add(a, b):
    c = a + b
    # 想要将求和的结果 c ,返回, 即函数外部使用求和的结果, 不在函数内部打印结果
    return c
    # print(f'求和的结果是{c}')     # 函数遇到return就结束了，不会执行 return之后的代码


# add(100, 200)
result = add(100, 200)
print(f'函数外部获得了求和的结果{result}')


# return 返回多个数据值
def func(a, b):
    c = a + b
    d = a - b
    # 需求: 想要将c 和 d, 都进行返回
    # 思考: 容器可以保存多个数据值 , 那就可以将c和d方到容器中进行返回
    return [c, d]  # 可以是 列表 元祖 字典
    # return c,d 默认是组成元祖进行返回的


result1 = func(100, 300)
print(f'a+b的结果是{result1[0]}, a-b的结果是{result1[1]}')

'''
# return 关键字后边可以不写数据值, 默认返回None
def function():
    ****
    return    # None, 终止函数的运行
    
    
'''

'''
函数可以不写 return ,返回值默认是 None
def function():
    ****
    pass
    
        
'''


# 函数的嵌套调用
def func1():
    print('fun1 start ... ')
    print('函数的其他代码')
    print('func1 end ... ')


def func2():
    print('func2 start ... ')
    func1()
    print('func2 end ... ')


# func1()
func2()    # 在一个函数中可以调用另外的一个函数


# / 除法运算得到的结果是 float类型

