# if 判断 输入年龄判断是否成年
age = input('请输入你的年龄:')  # str
# print('if判断开始')
age = int(age)  # int
if age > 17:
    print('我已经成年了')
else:
    print('我还没有成年')
# print('if判断结束')


# if elif elif else 结构中 ,只有一个条件满足成立,后续条件均不在判断
# 练习使用此结构
score = eval(input('请输入你的成绩:'))  # str
score = int(score)  # int
if score > 90:
    print('根据你的成绩,你被评为优秀')
elif (score >= 80) and score <= 90:
    print('你的成绩被评为良好,还需要努力')
elif score >= 60:    # 执行这个条件,前提是score<80
    print('你的成绩为中等,你的进步空间更大,加油')
else:
    print('你的成绩为差,请继续努力,加油 ,奥利给')

# if嵌套判断
money = int(input('请输入你的零钱:'))
if money >= 2:
    print('你可以乘车,你有足够的钱买车票 ')
    seat = int(input('请输入车上的空座位:'))
    if seat >= 1:
        print('有座位可以让你坐下')
    else:
        print('抱歉你只能站着了,车上没有座位了')
else:
    print('你不能乘车,因为你的零钱不够不能买车票,你只能走路回去了')

# 忘记是什么意思 看来是要写 注释
# 案例 需牢记
for i in 'fd':
    for j in 'hello world':
        print('hello world everyone')
    print()
    print(i)





