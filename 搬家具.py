"""
 类名  Furniture  家具
 属性
    类型 name type
   面积 ares
 方法
   输出家具信息   __str__
   定义属性   __init__
 ---------------
 类名 房子 house
 属性
   地址 address
   面积 h_ares
   家具列表  furniture_list = []
 方法
   添加家具 add_furniture
   输出房子信息 __str__
"""


# 定义家具类
class Furniture(object):
    def __init__(self, name, ares):    # 需不需要传参看数值是否一样 ,不一样需要传参
        # 类型
        self.name = name
        # 面积
        self.ares = ares


    def __str__(self):
        return f'家具的类型{self.name}, 占据面积{self.ares}'


# 创建家具对象
bed = Furniture('豪华双人床', 15)
print(bed)















