#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用正则表达式找出html文件中的所有链接，该文件为re_test.html
"""
import re


def find_all_link(file_name):
    # 打开文件
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()
    # 构造正则表达式对象
    link_regex = re.compile(r'"(http(s?)://([^"]+)\.([^"]+)\.com([^"]*))"')
    link_res = link_regex.finditer(file_content)  # 返回一个迭代器
    for i in link_res:
        print(i.group(1))  # 用group可以取出匹配成功的字符串中的一部分，这里取出的是""内包括的部分


if __name__ == '__main__':
    file_name = 're_test.html'
    find_all_link(file_name)
