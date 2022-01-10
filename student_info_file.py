Student = []


def menu():
    print("-" * 40)
    print("欢迎来到学生信息管理系统")
    print("[1] 增加学生信息")
    print("[2] 删除学生信息")
    print("[3] 修改学生信息")
    print("[4] 查询学生信息")
    print("[5] 保存学生信息")
    print("[6] 查询学生全部信息")
    print("[0] 退出系统")
    print("-" * 40)


def insert_stu_info():
    student = {}
    s_id = input("请输入学生学号：")
    for stu in Student:
        if s_id == stu['id']:
            print("你录入学生信息已存在！")
            break
    else:
        s_name = input("请输入学生姓名：")
        s_age = input("请输入学生年龄：")
        s_mobile = input("请输入学生电话号码：")
        student['id'] = s_id
        student['name'] = s_name
        student['age'] = s_age
        student['mobile'] = s_mobile
        print("添加成功！")
        Student.append(student)


def delete_stu_info():
    del_id = input("请输入需要删除学生的学号：")
    for student in Student:
        if student['id'] == del_id:
            Student.remove(student)
            print("学生信息删除成功！")
            break
    else:
        print("你输入的学生学号不存在，请重新输入！")


def update_stu_info():
    update_id = input("请输入要修改学生学号：")
    for student in Student:
        if student['id'] == update_id:
            update_name = input("请输入学生姓名：")
            update_age = input("请输入学生年龄：")
            update_mobile = input("请输入学生电话号码：")
            student['name'] = update_name
            student['age'] = update_age
            student['mobile'] = update_mobile
            print("学生信息修改成功！")
            print(student)
            break
    else:
        print("你输入的学生学号不存在，请重新输入！")


def select_student_info():
    select_id = input("请输入要查询学生学号：")
    for student in Student:
        if student['id'] == select_id:
            print("查询成功")
            print(student)
            break
    else:
        print("你输入的学生学号不存在，请重新输入！")


def save_stu_info():
    print(Student)
    with open("save_stu_info.txt", "w", encoding="utf-8") as f:
        for stu_list in Student:
            f.write(str(stu_list))
            f.write("\n")
        print("保存成功")


def load_stu_info():
    f = open("save_stu_info.txt", "r", encoding="utf-8")
    while True:
        data = f.readline()
        if data:
            # print(data, end="")
            Student.append(eval(data))
        else:
            break


load_stu_info()
while True:
    menu()
    user_num = int(input("请输入你要执行的功能编号："))

    if user_num == 0:
        print("感谢使用本系统！")
        break

    elif user_num == 1:
        insert_stu_info()

    elif user_num == 2:
        delete_stu_info()

    elif user_num == 3:
        update_stu_info()

    elif user_num == 4:
        select_student_info()

    elif user_num == 5:
        save_stu_info()

    elif user_num == 6:
        print("全部学生信息为：")
        for stu_info in Student:
            print(stu_info)

    else:
        print("你输入的编号有误，请重新输入！")
