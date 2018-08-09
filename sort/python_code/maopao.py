#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
冒泡排序
"""


def bubble_sort(ls):
    n = len(ls)
    for i in range(n-1):  # 共需要比较n-1轮
        for j in range(n-i-1):  # 每轮从开始位置比较至已排序前一个位置
            if ls[j] > ls[j+1]:
                ls[j+1], ls[j] = ls[j], ls[j+1]  # 交换位置

    return ls


if __name__ == '__main__':
    a = [7, 12, 2, 4, 1, 5, 2, 8, 16, 0]
    print("初始:%s" % a)
    print(bubble_sort(a))
