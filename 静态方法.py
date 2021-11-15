# 类方法 @classmethud 装饰的方法,称为类方法,第一个参数是 cls ,代表的是类对象自己
# 静态方法 @staticmethud 装饰的方法,称为静态方法 ,对参数没有特殊要求,可以有可以没有
# 什么情况 使用静态方法
#       前提 : 不需要使用实例属性 ,同时也不需要使用类属性,此时可以将这个方法定义为静态方法


class Dog(object):
    class_name = '狗类'

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def play(self):
        print('小狗在快乐的玩耍')

    @staticmethod
    def show_info():   # self 不用留 如果留必须传参
        print('这是一个dog类')


dog.Dog('大黄', 2)
dog.play()
# 调用方法
# 对象.方法名()
dog.show_info()

# 类名.方法()
Dog.show_info()























