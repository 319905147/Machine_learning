import random
print('1 代表 石头, 2 代表 布 , 3 代表 剪刀')

while True:

    user = int(input('请输入相关数字'))
    if 0 < user < 4:
        computer = random.randint(1, 3)
        print(computer)
        if user == computer:
            print('这一局是个平局')
        elif (computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1):
            print('玩家胜')
        else:
            print('电脑胜')
    else:
        print('请按照要求输入数字')














