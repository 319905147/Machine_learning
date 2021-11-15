# 如果 一个类有两个及以上的父类,就把这种继承关系称为多继承
# 1 定义一个 Dog 类,定义bark方法,和eat方法
# 2 定义God类,定义一个play方法,和eat方法
# 3 定义XTQ类,继承Dog 和God类
# 4 创建XTQ类对象
class Dog(object):
    def bark(self):
        print('汪汪汪叫')

    def eat(self):
        print('啃骨头')


class God(object):
    def play(self):
        print('在天上飘一会')

    def eat(self):
        print('吃蟠桃仙丹')


class XTQ(Dog, God):    # XTQ类 有两个父类,这个继承关系称为多继承,XTQ类对象,看可以调用两个父类中的属性和方法

    pass


xtq = XTQ()
xtq.bark()  # 调用Dog中的方法
xtq.play()  # 调用God中的方法

xtq.eat()   # 两个父类都存在eat方法 ,子类对象调用 第一个父类中的方法




















