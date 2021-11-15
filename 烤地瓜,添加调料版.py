class Potato(object):
    def __init__(self):
        self.status = '生的'
        self.total_time = 0
        self.name_list = []

    def cook(self, time):
        # 计算总时间
        self.total_time += time
        # 修改地瓜的状态
        if self.total_time < 3:
            self.status = '生的'
        elif self.total_time < 6:
            self.status = '半生半熟'
        elif self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '烤熟了'


    def __str__(self):
        if self.name_list:
            return f"地瓜的状态{self.status}, 烤地瓜的总时间为{self.total_time}, 调料有{self.name_list}"
        else:
            return f"地瓜的状态{self.status}, 烤地瓜的总时间为{self.total_time},还没有添加调料"

    def add(self, name):
        self.name_list.append(name)


# 创建对象
potato = Potato()
print(potato)
potato.add('油')
potato.cook(4)
print(potato)
potato.cook(7)
potato.add('孜然')
print(potato)







