"""
__all__ 变量,可以在每个代码文件中(模块中)定义,类型是元祖,列表
作用:只影响 from 模块名 import * 导入行为, 另外两种不受影响
1 如果没有定义这个__all__变量,,模块中的所有功能,都可以被导入
2 如果定义__all__变量,只能导入变量中定义的内容

"""


# 自己定义的模块名字,不要和系统中你要使用的模块名字相同
# 模块的搜索顺序,当前目录-->系统目录-->程序报错
"""
import sys
print(sys.path)  查找目录


"""







