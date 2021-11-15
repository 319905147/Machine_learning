

a = int(input('请输入第一个整数:'))
b = int(input('请输入第二个整数:'))
c = int(input('请输入第三个整数:'))

if a > b:
    if a > c:
        max = a
    else:
        max = c

else:
    if b > c:
        max = b
    else:
        max = c
print('max = ', max)





