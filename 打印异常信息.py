# 第一种写法
"""
try:
    可能发生异常的代码
except(异常的类型1, 异常类型2....) as 变量名:
      发生异常执行的代码
      print(变量名)
"""
print('其他代码')
num = input('请输入一个数字')
try:
    a = int(num)
    num = 10 / a
    print('计算的结果是 ', num)
except(ValueError, ZeroDivisionError) as f:
    print('你输入的有误,请再次输入')
    print(f)

print('其他代码')







