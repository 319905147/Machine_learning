# 第一种写法 :
#     try:
#             可能发生异常的代码
#     except(异常的类型1, 异常类型2....) :
#           发生异常执行的代码

print('其他代码')
num = input('请输入一个数字')
try:
    a = int(num)
    num = 10 / a
    print('计算的结果是 ', num)
except(ValueError, ZeroDivisionError):
    print('你输入的有误,请再次输入')

print('其他代码')

# 第二种类型:
"""
try:
    可能发生异常的代码
except异常类型1:
    异常类型1,执行的代码
except异常类型2:
    异常类型2,执行的代码
except...
    pass

"""

print('其他代码')
num = input('请输入一个数字')
try:
    a = int(num)
    num = 10 / a
    print('计算的结果是 ', num)
except ValueError:
    print('你输入不是数字,请再次输入')
except ZeroDivisionError:
    print('输入有误,请重新输入')
print('其他代码')













