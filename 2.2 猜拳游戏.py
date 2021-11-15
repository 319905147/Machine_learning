import random


print('------------欢迎来到猜拳小游戏------------')
print('在这里做一个简单的说下游戏规则,'
          '在这个游戏中数字 1 代表着石头'
          '数字 2 代表剪刀,数字 3 代表布')
print('牢记这些就可以有一个有趣的猜拳游戏')
while True:     # 无限循环
    user = int(input('请选择你要出的拳,:'))
    computer = random.randint(1, 3)
    print(computer)
    if user == computer:
        print('这一局是一个平局')
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        print('玩家胜')
    else:
        print('玩家输,电脑胜')
# break 终止循环
# continue 是终止这一次循环 ,下次循环仍然继续
