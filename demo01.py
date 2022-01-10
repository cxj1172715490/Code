import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory


# file1_name = "1.txt"
# index = file1_name.rfind(".")
# file2_name = file1_name[:index] + "[备份]" + file1_name[index:]

def choose_file():
    root = Tk()
    root.withdraw()
    # path = askdirectory(title='Choose file')
    filename = filedialog.askopenfile()
    # os.chdir(path)
    return filename.name


file1_name = choose_file()
index = file1_name.rfind(".")
file2_name = file1_name[:index] + "[备份]" + file1_name[index:]

list1 = file1_name.replace(".", "[beifen].")
# print(list1)

f1 = open(file1_name, "r")
f2 = open(file2_name, "w", encoding="utf-8")
while True:
    f1_data = f1.readlines()
    if f1_data:
        for i in f1_data:
            f2.write(i)
    else:
        break
print("备份完成！")
f1.close()
f2.close()

with open("./1.txt", "r") as f1:
    with open("./3.txt", "w", encoding="utf-8") as f2:
        data = f1.readlines()
        for i in data:
            f2.write(i)


def choose_file():
    root = Tk()
    root.withdraw()
    # path = askdirectory(title='Choose file')
    filename = filedialog.askopenfile()
    # os.chdir(path)
    return filename.name


# print(choose_file())
