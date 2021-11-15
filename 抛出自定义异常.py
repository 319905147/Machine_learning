# 程序代码为什么会报错?
# 因为不符合语法,本质:Python作者在代码中使用了 if 判断, 如果除数为 0 ,就会在代码中抛出异常
# 如何抛出异常?
"""
 使用关键字 raise
raise 异常对象    # 当程序代码遇到 raise 的时候,程序就报错了

"""

# 异常对象 = 异常类(参数)
# 抛出自定义异常:
#           1 自定义异常类: 继承Execption 或者 BaseExectpation
#           2 选择书写,定义 __init__ 方法,定义__str__方法
#           3 在合适的时机抛出异常即可


# 定义异常类,密码长度不足的异常
class PasswordLengthError(Exception):
    pass    # 继承父类的方法


def get_password():    # 等同于系统定义函数
    password = input('请输入密码')
    if len(password) >= 6:
        print('密码长度合格')
    else:
        # 抛出异常
        raise PasswordLengthError('密码长度不足6位')


try:
    get_password()
except PasswordLengthError as e:
    print(e)   # 异常类的 __str__ 方法

print('其他代码.....')
















