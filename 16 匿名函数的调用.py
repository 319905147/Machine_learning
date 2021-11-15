# 无参无返回值
def func1():
    print('hello world')


(lambda: print('hello Python'))()
func1()
f1 = lambda: print('hello Python')
f1()


# 无参有返回值
def func2():
    return 1 + 2


f2 = lambda: 1 + 2
print(f2())


# 3 有参数无返回值
def func3(name):
    print(name)


f3 = lambda name: print(name)
f3('hello')


# 4 有参数有返回值
def func4(a, *args):
    return args


f4 = lambda *args: args
print(f4(1, 2, 3, 4, 5))









