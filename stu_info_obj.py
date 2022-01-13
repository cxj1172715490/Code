import os


class Student(object):
    def __init__(self, s_no, s_name, s_age, s_mobile):
        self.s_no = s_no
        self.s_name = s_name
        self.s_age = s_age
        self.s_mobile = s_mobile

    def __str__(self):
        return f"学号：{self.s_no}，姓名：{self.s_name}，年龄{self.s_age}，电话{self.s_mobile}"


class StuManage(object):
    Students_list = []  # 定义类属性

    @staticmethod
    def menu():
        """
        定义静态方法
        """
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

    def insert_stu_info(self):
        s_no = input("请输入学生学号：")
        for stu_obj in StuManage.Students_list:
            if s_no == stu_obj.s_no:
                print("你录入学生信息已存在！")
                break
        else:
            s_name = input("请输入学生姓名：")
            s_age = input("请输入学生年龄：")
            s_mobile = input("请输入学生电话号码：")
            student_obj = Student(s_no, s_name, s_age, s_mobile)
            # 向类属性中添加信息
            StuManage.Students_list.append(student_obj)
            print("添加成功！")

    def delete_stu_info(self):
        del_id = input("请输入需要删除学生的学号：")
        for stu_obj in StuManage.Students_list:
            if stu_obj.s_no == del_id:
                StuManage.Students_list.remove(stu_obj)
                print("学生信息删除成功！")
                break
        else:
            print("你输入的学生学号不存在，请重新输入！")

    def update_stu_info(self):
        update_id = input("请输入要修改学生学号：")
        for stu_obj in StuManage.Students_list:
            if stu_obj.s_no == update_id:
                update_name = input("请输入学生姓名：")
                update_age = input("请输入学生年龄：")
                update_mobile = input("请输入学生电话号码：")
                stu_obj.s_name = update_name
                stu_obj.s_age = update_age
                stu_obj.s_mobile = update_mobile
                print("学生信息修改成功！")
                break
        else:
            print("你输入的学生学号不存在，请重新输入！")

    def select_student_info(self):
        select_id = input("请输入要查询学生学号：")
        for stu_obj in StuManage.Students_list:
            if stu_obj.s_no == select_id:
                print("查询成功")
                print(stu_obj)
                break
        else:
            print("你输入的学生学号不存在，请重新输入！")

    def save_stu_info(self):
        with open("stu_info.txt", "w", encoding="utf-8") as f:
            for stu_obj in StuManage.Students_list:
                f.write(str(stu_obj.__dict__))
                f.write("\n")
            print("保存成功")

    def __load_stu_info(self):
        if not os.path.exists("./stu_info.txt"):
            print("文件不存在，无法加载！")
            return
        f = open("stu_info.txt", "r", encoding="utf-8")
        while True:
            data = f.readline()
            if data:
                data = eval(data)
                stu_obj = Student(data["s_no"], data["s_name"], data["s_age"], data["s_mobile"])
                StuManage.Students_list.append(stu_obj)
                print(stu_obj)
            else:
                break

    def main(self):

        self.__load_stu_info()  # 加载数据

        while True:
            StuManage.menu()

            user_num = input("请输入你要执行的功能编号：")

            if user_num == "0":
                print("感谢使用本系统！")
                break

            elif user_num == "1":
                self.insert_stu_info()

            elif user_num == "2":
                self.delete_stu_info()

            elif user_num == "3":
                self.update_stu_info()

            elif user_num == "4":
                self.select_student_info()

            elif user_num == "5":
                self.save_stu_info()

            elif user_num == "6":
                print("全部学生信息为：")
                for stu_obj in StuManage.Students_list:
                    print(stu_obj)

            else:
                print("你输入的编号有误，请重新输入！")


if __name__ == '__main__':
    student = StuManage()
    student.main()
