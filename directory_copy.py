"""
题干：使用进程实现文件夹的整体拷贝。
    在拷贝文件夹的文件时，如果文件夹中的文件很多，那么一个一个拷贝，效率会很低下，那么可以使用多任务的形式来实现文件夹下的文件进行同时拷贝，
    提高拷贝效率。请写出一个程序实现这个功能！
"""

import multiprocessing
import os


def file_copy(src_file, dest_file):
    """
    单个文件的复制
    :param src_file: 要复制文件的源路径
    :param dest_file: 要复制文件的目标路径
    :return:
    """
    f_r = open(src_file, "r", encoding="utf-8")
    f_w = open(dest_file, "w", encoding="utf-8")
    while True:
        data = f_r.readline()
        if data:
            f_w.write(data)
        else:
            break
    f_r.close()
    f_w.close()
    print(f"{src_file} -> {dest_file}")


def dir_copy(src, dest):
    """
    在文件夹中开启进程实现文件复制
    :param src: 要复制的文件源路径
    :param dest: 要复制文件的目标路径
    :return: None
    """
    # 如果目标文件不存在则创建，存在则直接使用
    if not os.path.exists(dest):
        os.mkdir(dest)
    # 获取目录中的文件
    file_list = os.listdir(src)
    for i in file_list:
        sub_process = multiprocessing.Process(target=file_copy, args=(src+"/"+i, dest+"/"+i))
        sub_process.start()


if __name__ == '__main__':
    src = "D:/Desktop/Code/PythonCode/day16/test"
    dest = src + "_copy"
    dir_copy(src, dest)
