#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
选择排序

- 首先在未排序序列中找到最大或最小的元素，存放到排序序列的起始(或末尾)位置（与原位置的元素进行交换），然后再从剩余未排序的元素中继续寻找最大或最小的元素，
将其存放到已排序序列的末尾。以此类推，直至排序完成。

- 选择排序的主要优点与数据移动有关。它每次只交换一对元素，每一轮交换至少有一个元素被移动到最终位置，因此对n个元素的表进行排序至多需要n-1次交换
（若某元素位于正确位置，则不需要交换）。

- 在完全依靠交换去移动元素的排序中，选择排序是很好的一种算法
"""


def select_sort(lst):

    for i in range(len(lst)):
        # 假设找到的最小元素的下标为i
        min_index = i
        # 寻找最小元素
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        # 将最小元素和初始元素进行交换
        if min_index != i:  # 如果等于，则说明在正确的位置，没必要交换
            lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst


if __name__ == "__main__":
    a = [7, 12, 2, 4, 1, 5, 2, 8]
    print(select_sort(a))


