# 多态  在使用父类对象的地方,也可以使用子类对象,得到不同的结果    这种情况叫做多态
#  比如 ,在函数中,我需要调用某一个父类对象的方法,那么我们也可以在这个地方调用子集对象的方法
# 实现步骤  :

#   1 子类继承父类
#   2 子类重写父类的同名方法
#   3 定义一个共同的额方法,参数为父类对象,在方法中调用子类和父类同名的方法

#
# 定义 一个Dog类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'小狗{self.name} 在玩耍')


# 定义XTQ类
class XTQ(Dog):
    # 重写 play方法
    def play(self):
        print(f'{self.name}再追云彩')


# 定义一个共同的方法
def play_with_dog(obj_dog):
    obj_dog.play()


# 创建Dog类对象
dog = Dog('大黄')
play_with_dog(dog)

# 创建一个xtq类
xtq = XTQ('小黑')
play_with_dog(xtq)








