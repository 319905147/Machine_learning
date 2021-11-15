# 描述的是类与类之间的所属关系
# 如果一个类 A里面的属性和方法可复用,则可以通过继承的方式,传递到类B里
# 那么 类A技术基类,也叫父类,  类B就是派生类,也叫做 子类
# 基本语法 :

"""

class 类B(类A):
    pass

称为 类 B 继承 类 A ,
特点 : B类中的对象,可以使用 A类的属性和方法
优点: 代码复用,重复相同的代码,不用多次书写

名词:
 类 A :  父类  基类
 类 B :  子类  派生类


"""


# 1 定义一个 动物类 animal 类
class Animal(object):
    # 2 在animal 类 书写 play方法,输出快乐的玩耍
    def play(self):
        print('快乐的玩耍...')


# 3 定义一个dog 类 ,继承animal类
class Dog(Animal):
    pass


# 4 创建dog类 对象,调用animal类的方法
dog = Dog()
dog.play()

































