# 元祖和列表非常相似,都可以存放多个数据,可以存放不同的数据类型
# 不同点:列表使用[],元祖使用()
# 列表中的数据可以修改,元祖中的数据不能修改


my_list = [1, 3, 'hello ']  # 列表
my_tuple = (1, 3, 'hello ')  # 元祖
print(my_tuple, type(my_tuple))
# 元祖支持下标和切片
print(my_tuple[1])

# 定义空元祖,空元祖没有意义
my_tuple1 = ()
print(my_tuple1, type(my_tuple1))

my_tuple2 = tuple()  # 这样也可以定义一个空元祖

# 定义一个数据的元祖,数据元素后边必须有一个  ,
my_tuple3 = (5)
print(my_tuple3, type(my_tuple3))   # 5 <class 'int'>

my_tuple4 = (5,)    # 定义一个数据的元祖,需要在数据后加一个  ,
print(my_tuple4, type(my_tuple4))   # (5,) <class 'tuple'>



