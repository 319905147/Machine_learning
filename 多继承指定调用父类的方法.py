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


class XTQ(Dog, God):  # XTQ类 有两个父类,这个继承关系称为多继承,XTQ类对象,看可以调用两个父类中的属性和方法
    def eat(self):
        print('子类重写eat方法,调用子类自己的方法')
    # 调用指定父类的方法
    # 方法一 类名.方法名(self, 其他参数)
        Dog.eat(self)
        God.eat(self)
    # 方法二 super(类 A, self).方法名(参数)   类A的父类(继承的顺序链的下一个类)中的方法
        super(XTQ, self).eat()          # God类中的方法
        super(Dog, self).eat()    # Dog 类中的方法

        # super(God, self).eat()      # 调用的是object中的方法  注意:object 中没有eat方法,代码报错



xtq = XTQ()
xtq.bark()  # 调用Dog中的方法
xtq.play()  # 调用God中的方法

xtq.eat()  # 两个父类都存在eat方法 ,子类对象调用 第一个父类中的方法


"""
# 类名.__mro__ 可以查看当前类的继承顺序链也叫做方法的调用顺序
print(XTQ.__mro__)
# (<class '__main__.XTQ'>, <class '__main__.Dog'>, <class '__main__.God'>, <class 'object'>)

"""



























