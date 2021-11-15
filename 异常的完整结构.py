"""
try:
    可能发生异常的代码
except Exception as f:
    发生异常是执行的代码
    print(f)
else:
    代码没有发生异常会执行
finally:
    不管有没有发生异常都会执行
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
else:
    print('没有发生异常,我会执行')
finally:
    print('不管有没有异常我都会执行')
print('其他代码')






















