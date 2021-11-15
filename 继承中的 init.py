# 1 定义Dog类
class Dog(object):
    def __init__(self, name):
        # 添加属性
        self.age = 0
        self.name = name

    def __str__(self):
        return f'年龄为{self.age}, 名字为{self.name}'


# 定义XTQ 类继承Dog类
class XTQ(Dog):
    # 子类重写了父类的 __init__方法,默认不在调用 父类的 __init__方法,需要手动的调用父类的 __init__方法
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def __str__(self):
        return f'年龄为{self.age}, 名字为{self.name}, 毛色为{self.color}'

# 如果子类重写了父类的init方法,在子类中需要调用父类的init方法,给对象添加从父类继承的属性
# 子类 init方法的形参,一般先写父类的形参,再写子类自己独有的形参



# 创建XTQ类的一个对象
xtq = XTQ('小黑', '红色毛发')
print(xtq)





















