#!/usr/in/env python
# -*- coding: utf-8 -*-

"""
最大子序列的和

穷举法，设定一个初始最大值，计算出所有连续子序列的最大和，与初始值进行比较，得到最大的
"""


def max_sub_seq(lst):
    # 初始化
    max_seq_sum = lst[0]

    for i in range(len(lst)):
        # 计算从i开始的子序列的和
        now_sum = lst[i]
        for j in range(i+1, len(lst)):
            # if lst[j] < 0:
            #     break
            # else:
            #     now_sum += lst[j]
            now_sum += lst[j]
        if max_seq_sum < now_sum:
            max_seq_sum = now_sum
    return max_seq_sum


if __name__ == '__main__':
    a = [-1, 0, 2, 4, 6, -3, 2, 3, 10]
    print(max_sub_seq(a))



