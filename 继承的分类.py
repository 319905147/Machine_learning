# ?????: ???????? ??????????,???????й??????????
# ????:?????????ж??????,???????й?????????
# ?????:


# 1 ??????? ?????? animal ??
class Animal(object):    # ????Animal???object?????,?????
    # 2 ??animal ?? ??д play????,???????????
    def play(self):
        print('????????...')


# 3 ???????dog ?? ,???animal??
class Dog(Animal):    # Dog--->Animal??????? ,Dog--->Animal--->object ?????й??????????
    def bark(self):
        print('??????')
    pass


# ????????? XTQ,???Dog??
# ???????,?????????????м?????е????е?????????
class XTQ(Dog):     # XTQ --->Dog ?????    ,  XTQ ---> Animal?? ,?????
    pass


# 4 ????dog?? ????,????animal??????
dog = Dog()
dog.play()

xtq = XTQ()
xtq.bark()
xtq.play()

