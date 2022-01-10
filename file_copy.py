import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory


# 定义函数，生成界面框选择文件
def choose_file():
    root = Tk()
    root.withdraw()
    # path = askdirectory(title='Choose file')  # 选择文件文件夹
    filename = filedialog.askopenfile()  # 选择文件
    # os.chdir(path)
    return filename.name


file1_name = choose_file()
index = file1_name.rfind(".")  # 从右向左查找
file2_name = file1_name[:index] + "[备份]" + file1_name[index:]  # 拼接成新文件名称

# file1_name = "1.txt"
# index = file1_name.rfind(".")
# file2_name = file1_name[:index] + "[备份]" + file1_name[index:]


f1 = open(file1_name, "r")  # 打开文件
f2 = open(file2_name, "w", encoding="utf-8")
while True:
    f1_data = f1.readlines()  # readline逐行读取；readlines全部读取
    if f1_data:
        for i in f1_data:
            f2.write(i)  # 将数据写入文件
    else:
        break
print("备份完成！")
f1.close()  # 关闭文件流
f2.close()

with open("./1.txt", "r") as f1:  # 文件自动关闭
    with open("./3.txt", "w", encoding="utf-8") as f2:
        data = f1.readlines()
        for i in data:
            f2.write(i)

