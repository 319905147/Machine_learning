# 递归 函数自己嵌套调用自己
# 递归形成条件:1 函数自己调用自己
#            2 函数必须有一个终止条件
# 缺点 占据大量内存
def get_age(num):
    """
    求第 num 个人的年龄,每相邻的两个人的年龄差两岁 已知第一个人的年龄是18岁

    :return:
    """
    if num == 1:
        return 18
    # 求 第 num 个人的年龄,只需要num-1 这个人的年龄加2
    age = get_age(num-1) + 2
    return age


print(get_age(1))
print(get_age(5))


print('=='*10)
# 普通法求阶乘


def func(n):
    num = 1
    for i in range(1, n + 1):
        num = num * i
    print(num)


func(5)
# 用递归函数求阶乘


def func2(n):
    # 想要求n!, 只需要(n-1)*n
    if n == 1:
        return 1

    num = func2(n-1) * n
    return num


print(func2(5))










