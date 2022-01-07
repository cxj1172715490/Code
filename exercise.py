import random

# 练习题1：输入一个字符串，打印所有奇数位上的字符(下标是1，3，5，7…位上的字符)
_str = "asdfghjklpoiuytrewq"
for i in range(len(_str)):
    if i % 2 != 0:
        print(_str[i])

# 练习题2：给定一个文件名，判断其尾部是否以".png"结尾
file_name = "cat.png"
if file_name.endswith(".png"):
    print("该文件是.png结尾")
else:
    print("该文件不是.png结尾")

"""
练习题3：给定一个字符串，如：
mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
使用所学的知识，从字符串中随机取出4个字符，生成验证码。
"""
mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
random_str = random.sample(mystr, 4)
print("".join(random_str))

# 1、有两个列表list1 = [11, 22, 33]，list2 = [22, 33, 44]，获取两个列表中相同的元素，结果22与33
list1 = [11, 22, 33]
list2 = [22, 33, 44]
for i in list1:
    for j in list2:
        if i == j:
            print("两个列表中的相同元素有：", i)
            break

"""
2、列表嵌套：有3个教室[[],[],[]]，8名讲师['A','B','C','D','E','F','G','H']，将8名讲师随机分配到3个教室中
"""
room_list = [[], [], []]
teacher_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for i in range(len(teacher_list)):
    t_popList = teacher_list.pop()
    num = random.randint(0, 2)
    room_list[num].append(t_popList)
print(room_list)
