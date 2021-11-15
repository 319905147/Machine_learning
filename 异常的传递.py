# 是Python 异常处理的底层机制,是原理成面上的,不需要我们子集写代码实现,是Python已经实现好的
# 异常的传递: 当一行代码发生异常之后,回乡外层传递直到被捕获或者程序报错为止
#
# # 两种情况
# # 1 try嵌套
# print('其他功能代码')
# num = input('请输入 数字')
# try:
#     try:
#         a = int(num)  # 内层try代码发生的异常,没有被捕获,回向外层传递
#
#     except ZeroDivisionError:
#         print('发生异常')
#     finally:
#         print('总是会执行')
#     num = 10 / a
#     print(f'计算的结果是 {num}')
# except Exception as e:
#     print(e)
#
# print('其他功能代码')


# 2 函数的传递
def func1():
    print('-----1-----')
    num = input('请输入一个数字')
    num = 10 / int(num)
    print(num)
    print('-----2-----')


def func2():
    print('------3------')
    func1()
    print('------4-------')


try:
    print('-----5-----')
    func2()
    print('------6----')
except Exception as e:
    print('-------7------')
    print(e)




