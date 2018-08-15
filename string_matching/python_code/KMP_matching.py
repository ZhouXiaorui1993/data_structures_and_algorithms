#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
字符串匹配的非平凡算法——KMP算法

该算法的基本思想是匹配中不回溯，在匹配失败时把模式串前移若干位置，用模式串里匹配失败字符之前的某个字符与目标串中匹配失败的字符比较

实现这种算法的关键在于确定匹配失败时模式串如何前移

对于模式串p中的每个i，都有与之对应的下标k_i，与被匹配的目标串无关。为此可以考虑用一个长为m的表pnext，用表元素pnext[i]记录与i对应的k_i值

算法时间复杂度：O(n)，n为目标串的长度
"""


def gen_pnext(p):
    """
    计算pnext表，表中存储的是对应部分的部分匹配值（Partial Match Table），即前缀和后缀的最长共有元素的长度
    所谓前缀，指除了最后一个字符之外，一个字符串的全部头部组合；后缀则是除了第一个字符之外，一个字符串的全部尾部组合
    例如：
    ”A“:前缀和后缀均为空，部分匹配值为0
    ”AB“：0
    ”AA“:1
    "ABA":1
    "ABCDAB":2
    """
    i, k, m = 0, 0, len(p)
    # 初始化数组全为0
    pnext = [0]*m
    # 显然第一个字符的最大相同前后缀的长度为0，故从第二个字符开始计算
    for i in range(1, m):
        # 已知上一步计算得到的最大相同前后缀的长度为k（k>0），即p[0]...p[k-1]为最大相同前/后缀
        while k>0 and p[i] != p[k]:
            # 若不能匹配，则递归去比较上一个最大相同前后缀的下一个字符（下标即为上一个最大相同前后缀的长度）
            k = pnext[k-1]
        # 若能匹配，则此位置的最大相同前后缀的长度为k（k不一定是上一次的，是由上面的递推循环得到的结果）加1
        if p[i] == p[k]:
            k = k+1
        pnext[i] = k
    return pnext


def matching_KMP(target_str, pattern_str):
    """
    KMP串匹配的主函数
    """
    n, m = len(target_str), len(pattern_str)
    # i为p的计数下标，j为t的计数下标
    j, i = 0, 0
    # 生成部分匹配表
    pnext = gen_pnext(pattern_str)

    for j in range(n):
        while i > 0 and pattern_str[i]!= target_str[j]:
            # 当遇到不能匹配的字符（此时最后一个匹配的字符是pattern_str[i-1]）
            # 现在要移动模式串，将前缀与后缀对齐，比较前缀后面一位字符和目标串上一次失配的字符
            # 因此，需要将比较索引设置为前缀的长度
            i = pnext[i-1]
        if pattern_str[i] == target_str[j]:
            i = i+1
        if i == m:
            return j-m+1  # 找到，返回子串起始坐标
    return -1   # 未找到，则返回-1


if __name__ == '__main__':
    target_str = "abbbdbdcdejjdskssabbb"
    pattern_str = "skss"
    print(matching_KMP(target_str, pattern_str))


