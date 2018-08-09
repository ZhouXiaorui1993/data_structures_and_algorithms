#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
插入排序
- 将原序列视为两部分，左边是已经排好序的，右边是未排序的
- 最开始左边只有一个数，即lst[0]，然后从右边开始逐个取数，向左边插入，通过与左边的元素逐一比较来确定插入的位置
"""


def insert_sort(lst):

    # 左边已有一个数，视为排好序的部分，因此共需要比较n-1轮(从第二个到最后一个)
    for i in range(1, len(lst)):
        # 待插入的数
        x = lst[i]
        # 从i-1处开始向左与左边的数逐一比较，若待插入的数大于该数，插入在该数之后；若小于，则序列右移，为在前面插入留出空位
        for j in range(i, -1, -1):
            if x < lst[j-1]:
                lst[j] = lst[j-1]
            # 待插入的数较大时，直接退出循环（比较完毕也会退出循环）
            else:
                break
        # 退出循环时，j即为要插入的位置索引
        lst[j] = x
    return lst


if __name__ == '__main__':
    a = [7, 12, 2, 4, 1, 5, 2, 8, 16, 0]
    print("初始:%s" % a)
    print(insert_sort(a))