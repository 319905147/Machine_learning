# 一个学校有3个办公室(学校是一个列表,里边每个办公室又是一个列表)
# 将8个老师进行分配(这8个老师共同组成一个列表)
# 采取抓阄,即电脑产生随机数
# for 遍历老师列表,根据随机数进入对应办公室


import random
# while True:
# 1 定义学校列表
schools = [[], [], []]   # 里边每个小列表为一个办公室,下标为 0 1 2
# 2 定义老师列表
teacher_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 3 让老师抓阄
for teacher in teacher_names:
    # 产生随机数
    num = random.randint(0, 2)  # 产生的随机数相当于是办公室的下标
    # randint()是唯一一个包括末尾的

    schools[num].append(teacher)        # 让老师进入办公室, 蒋老师名字添加到列表中
print(schools)
for office in schools:
    print(f'办公室老师的个数为{len(office)}, 办公室老师的名字为:')
    for teacher in office:
        print(teacher, end='')
    print()