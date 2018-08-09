#!/usr/in/env python
# -*- coding: utf-8 -*-

"""
最大子序列的和

动态规划法，时间复杂度为O(n)

由于最大连续子序列的和只可能在以位置0~n-1的某个位置结尾，当遍历到第i个元素时，判断在它前面的子序列和是否大于0，
如果大于0，则以位置i结尾的最大连续子序列和为元素i和前面的连续子序列相加；否则，以位置i结尾的最大连续子序列和为元素i


"""


def max_sub_seq(lst):
    max_sum = lst[0]
    this_sum = lst[0]

    for i in range(1, len(lst)):
        # 若前面位置最大连续子序列和小于等于0，则以当前位置结尾的最大连续子序列和为当前元素
        if this_sum <= 0:
            this_sum = lst[i]
        else:
            this_sum += lst[i]
        # 将以i结尾的最大子序列的和与max_sum比较，若this_sum较大，则更新max_sum的存储值
        if this_sum > max_sum:
            max_sum = this_sum

    return max_sum


if __name__ == '__main__':
    a = [-1, 0, 2, 4, 6, -3, 2, 3, 10]
    print(max_sub_seq(a))



