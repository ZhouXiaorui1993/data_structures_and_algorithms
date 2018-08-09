#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
快速排序的递归实现
- 取第一个元素作为基准元素
- 用挖坑法实现分组
"""


def partition(ls, start_index, end_index):
    # 基准元素
    pivot = ls[start_index]

    # 定义左右索引指针分别指向首尾元素
    left_pt = start_index
    right_pt = end_index

    # 当左指针大于右指针时，退出循环
    while left_pt < right_pt:
        # 从右边开始遍历，找到小于基准元素的元素
        while left_pt < right_pt and ls[right_pt] >= pivot:
            # 右指针左移
            right_pt -= 1
        # 将小于基准元素的元素，填入坑中，则右指针处变成了新的坑，同时通过交换将基准元素放入新的坑中
        if left_pt < right_pt:
            ls[left_pt], ls[right_pt] = ls[right_pt], ls[left_pt]
            # ls[left_pt] = ls[right_pt]
            # # 左指针右移
            # left_pt += 1

        # 从左边开始向右遍历，找到大于基准元素的元素
        while left_pt < right_pt and ls[left_pt] <= pivot:
            # 若小于，左指针右移
            left_pt += 1
        # 找到小于基准元素的元素，将其填入坑中
        if left_pt < right_pt:
            ls[right_pt], ls[left_pt] = ls[left_pt], ls[right_pt]
            # ls[right_pt] = ls[left_pt]
            # right_pt -= 1  # 利用交换的方式填坑，无需将指针左移，因为下一次循环中，指针将自动左移，所以该语句可有可无

    # 当左右指针重合时，退出上述循环
    # 将基准元素放入该位置，完成一次分组
    # ls[left_pt] = pivot  # 如果利用交换的方式填坑，则完成后自动会将基准元素放入
    return left_pt


def quick_sort_wk(ls, left, right):
    if left < right:
        pivot_index = partition(ls, left, right)
        # 对分组递归排序
        quick_sort_wk(ls, left, pivot_index)  # 左侧
        quick_sort_wk(ls, pivot_index + 1, right)


if __name__ == '__main__':
    a = [7, 12, 2, 4, 1, 5, 2, 8]

    quick_sort_wk(a, 0, len(a) - 1)

    print(a)