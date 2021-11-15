
# 1+2+...+100  累加
my_sum = 0
i = 1
while i <= 100:
    my_sum += i
    i += 1
print('输出得结果是', my_sum)



# 操场跑步每跑一圈做3个俯卧撑
# while 循环
a = 0
while a < 5:
    print('跑步一次')
    a += 1
    b = 0
    while b < 3:
        print('做三个俯卧撑')
        b += 1
a += 1

# for循环
for i in range(5) :
    print('操场跑圈圈')
    for j in range(3):
        print('做一次俯卧撑')


# 打印正方形
# while 循环
# n = int(input('请输入正方形的边长:'))
n = 5
i = 0
while i < n:
    j = 0
    while j < n:
        print('*', end=' ')
        j += 1
    print()     # 默认添加换行
    i += 1
"""
# 循环打印三角形
# while 循环
n = 5
i = 1
while i < n:
    j = 1
    while j < i+1:
        print('*', end=' ')
        i += 1
    print()
    j += 1

"""



# 循环打印三角形
# for循环
for i in range(5):
    for i in range(i+1):
        print('*', end=' ')
    print()



