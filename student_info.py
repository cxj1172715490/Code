import pymysql

# 连接本地数据库
db = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="jie081123", database="Student")
cur = db.cursor()

def menu():
    """
    创建功能选项菜单
    """
    print("-" * 40)
    print("欢迎来到学生信息管理系统")
    print("[1] 增加学生信息")
    print("[2] 删除学生信息")
    print("[3] 修改学生信息")
    print("[4] 查询学生信息")
    print("[5] 查看所有学生信息")
    print("[0] 退出系统")
    print("-" * 40)


def select_data(param):
    """
    根据用户输入学号查询学生信息。
    :param param:学生学号
    :return:学生学号对应的学生信息
    """
    select_sql = "select s_no, s_name, s_age, s_mobile from student_info where s_no = '%s';" % param
    cur.execute(select_sql)
    stu_infos = cur.fetchall()
    if len(stu_infos) > 0:
        for stu_info in stu_infos:
            return stu_info
    else:
        return None


def select_all_data():
    """
    查询所有学生信息
    :return: 所有学生信息
    """
    select_all_data_sql = "select s_no, s_name, s_age, s_mobile from student_info;"
    cur.execute(select_all_data_sql)
    res = cur.fetchall()
    all_stu = []
    title_list = ["s_no", "s_name", "s_age", "s_mobile"]
    for stu in res:
        stu_dict = dict(zip(title_list, stu))
        all_stu.append(stu_dict)
    return all_stu


def insert_data():
    """
    跟据用户输入插入学生信息
    :return:
    """
    s_no = input("请输入学生学号：")
    if select_data(s_no) != None:  # 跟据学号查询不到学生信息则执行插入功能，否则提示
        print("该学生学号信息已存在本系统！")
    else:
        s_name = input("请输入学生姓名：")
        s_age = int(input("请输入学生年龄："))
        s_mobile = input("请输入学生电话号码：")
        insert_sql = "insert into student_info values (null, '%s', '%s', %d, '%s');" % (
            s_no, s_name, s_age, s_mobile)
        try:
            cur.execute(insert_sql)
            db.commit()
            print("学生信息插入成功！")
        except Exception as e:
            print(e)
            db.rollback()
            print("学生信息插入失败！")


def delete_data(param):
    """
    跟据用户输入学号删除对应学生信息
    :param param: 学生学号
    :return:
    """
    student = select_data(param)
    if student is None:
        print("暂未查询到该学号对应的学生信息，请确认删除信息是否正确！")
    else:
        delete_sql = "delete from student_info where s_no = '%s';" % param
        try:
            cur.execute(delete_sql)
            db.commit()
            print("学生信息删除成功！")
        except Exception as e:
            db.rollback()
            print("学生信息删除失败！")
            print(e)


def update_data():
    """
    修改学生信息
    :return:
    """
    update_no = input("请输入要修改学生学号：")
    stu_info = select_data(update_no)
    if stu_info == None:
        print("该学生信息暂未录入！请重新输入")
    else:
        print("学号为{}的学生信息如下：".format(update_no))
        print(stu_info)
        print("请输入修改后的学生信息！")
        update_name = input("请输入学生姓名：")
        update_age = int(input("请输入学生年龄："))
        update_mobile = input("请输入学生电话号码：")
        update_sql = 'update student_info set s_name = "%s", s_age = "%d", s_mobile = "%s" where s_no = "%s";' % \
                     (update_name, update_age, update_mobile, update_no)
        # print(update_sql)
        cur.execute(update_sql)
        db.commit()
        print("学生信息修改成功！")


while True:
    menu()
    user_num = int(input("请输入你要执行的功能编号："))

    if user_num == 0:  # 退出系统
        print("感谢使用本系统！")
        break

    elif user_num == 1:  # 添加学生信息
        insert_data()

    elif user_num == 2:  # 删除学生信息
        del_no = input("请输入需要删除学生的学号：")
        delete_data(del_no)

    elif user_num == 3:  # 更新学生信息
        update_data()

    elif user_num == 4:  # 查询学生信息
        select_no = input("请输入要查询学生学号：")
        student_info = select_data(select_no)
        if student_info is None:
            print("暂未查询到该学生信息！")
        else:
            print("学生信息为：", student_info)

    elif user_num == 5:  # 查询全部学生信息
        all_stu_info = select_all_data()
        for stu_info in all_stu_info:
            print(stu_info)

    else:
        print("你输入的编号有误，请重新输入！")
