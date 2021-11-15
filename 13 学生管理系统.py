"""
学生管理系统
对学生信息进行 添加 删除 修改 查询
每一个学生信息为一个字典
把学生信息储存在列表中
王建彬
2021.10.12
"""


# 定义学生列表,保存所有的学生信息
stu_list = []


def show_menu():

    print('1,添加学生信息')
    print('2,删除学生信息')
    print('3,修改学生信息')
    print('4,查询单个学生信息')
    print('5,查询全部学生信息')
    print('6,退出系统')


def insert_student():
    # 1.通过input函数获取学生的信息  (姓名,年龄,性别)
    name = input('请输入学生的姓名:')
    # 代码优化  假设学生的姓名都不能重复,再添加学生的时候,进行判断,如果学生名字已经存在,则不添加
    # [{} {} {}] 判断的是字典的value 是否存在  使用遍历
    for stu in stu_list:
        if stu['name'] == name:
            print('------这个学生信息存在------')
            return  # 结束函数的执行
    age = input('请输入学生的年龄:')
    gender = input('请输入学生的性别:')
    # 2.将学生的信息转换为字典进行保存
    stu_dict = {'name': name, 'age': int(age), 'gender': gender}
    # 3.将这个学生字典添加到列表中
    stu_list.append(stu_dict)
    print('==========学生信息添加成功==========')


# 删除 修改 查询 学生信息
def remove_student():
    # 1 都使用 name 对学生进行判断
    # 2 使用 input 获取要 删除 的学生姓名
    name = input('请输入需要操作的学生的姓名:')
    # 3 判断学生的信息是否存在
    for student in stu_list:
        if student['name'] == name:
            # 4 学生存在对学生进行 删除
            stu_list.remove(student)
            print('该学生信息已经成功删除')
            # return
            break
    # 5 学生信息不存在,直接结束
    else:
        print('-*-----该学生的信息不存在无法删除-----*-')


def modify_student():
    # 1 都使用 name 对学生进行判断
    # 2 使用 input 获取要 修改 的学生姓名
    name = input('请输入需要操作的学生的姓名:')
    # 3 判断学生的信息是否存在
    for student in stu_list:
        if student['name'] == name:
            # 4 学生存在对学生进行 修改
            student['age'] = int(input('请重新输入年龄'))
            student['gender'] = input('请重新输入性别')
            # return
            break
    # 5 学生信息不存在,直接结束
    else:
        print('-*-----该学生的信息不存在,无法修改-----*-')


def search_student():
    # 1 都使用 name 对学生进行判断
    # 2 使用 input 获取要 查询 的学生姓名
    name = input('请输入需要操作的学生的姓名:')
    # 3 判断学生的信息是否存在
    for student in stu_list:
        if student['name'] == name:
            # 4 学生存在对学生进行 查询
            print(f'姓名:{student["name"]},年龄:{student["age"]},性别:{student["gender"]}')
            # return
            break
    # 5 学生信息不存在,直接结束
    else:
        print('-*-----该学生的信息不存在无法查询-----*-')


def show_all_student():
    if len(stu_list) > 0:
        for student in stu_list:
            print(f'姓名:{student["name"]},年龄:{student["age"]},性别:{student["gender"]}')
            # print(student)
    else:
        print('目前还没有学生信息')


def main():
    while True:
        show_menu()
        opt = input('请输入要选择进行的操作编号: ')
        if opt == '1':
            # print('1, 添加学生信息')
            insert_student()
        elif opt == '2':
            # print('2,删除学生信息')
            remove_student()
        elif opt == '3':
            # print('3,修改学生信息')
            modify_student()
        elif opt == '4':
            # print('4,查询单个学生的信息')
            search_student()
        elif opt == '5':
            # print('5,查询全部学生信息')
            show_all_student()
        elif opt == '6':
            print('-*-*-*-*-*-*-欢迎下次使用本系统-*-*-*-*-*-*-')
            break
        else:
            print('输入有误,请输入正确的编号(1-6)')
            continue

        input('------回车键继续操作------')

main()






