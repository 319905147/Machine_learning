# 捕获所有类型的异常:
# 方法一
"""
try:
    可能会发生异常的代码
except:       # 缺点,不能获取异常的描述信息
    发生异常执行的代码
"""

# 方法二
"""
try:
    可能发生异常的代码
except Exception as f:
    发生异常是执行的代码
    print(f)
    pass
    
  Exception   是常见异常类的父类
    
"""











