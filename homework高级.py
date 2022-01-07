# 题目二
"""
1，判断单词great是否在这个字符串中，如果在，则将每一个great后面加一个s， 如果不在则输出 great不在该字符串中,
   字符串为: " great craTes Create great craters, But great craters Create great craters "
2，将整个字符串的每一个单词都变成小写，并使每一个单词的首字母变成大写
3，去除首尾的空白，并输出处理过后的字符串
"""
_str = " great craTes Create great craters, But great craters Create great craters "
# 1
if _str.find("great") != -1:
    new_str = _str.replace("great", "greats")
    print(new_str)
else:
    print("great不在该字符串中")

# 2
low_str = _str.lower().title()
print(low_str)

# 3
str1 = _str.strip(" ")
print(str1)

# 题目三
"""
将下列两个列表合并，将合并后的列表去重，之后降序并输出
list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]
"""
list1 = [11, 45, 34, 51, 90, 0]
list2 = [4, 16, 23, 0]
list1.extend(list2)
new_list = list(set(list1))
new_list.sort(reverse=True)
print(new_list)

# 题目四
"""
现有列表：
namelist =["tom","kaisa","alisi",["xiaoming","songshu"]]
现在有个要求，将最外层的列表转换成元组存储，里面的小列表不变；
并且向小列表中添加一个元素“python”
"""
namelist = ["tom", "kaisa", "alisi", ["xiaoming", "songshu"]]
tup_list = tuple(namelist)
tup_list[-1].append("python")
print(tup_list)
