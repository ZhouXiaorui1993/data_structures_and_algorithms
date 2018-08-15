#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
朴素的串匹配算法：
1. 从左到右逐个字符比较
2. 发现不匹配时，转而去考虑目标串里的下一个位置是否与模式串匹配

算法时间复杂度：O(m×n)
"""

def naive_matching(target_str, pattern_str):
    m, n = len(target_str), len(pattern_str)
    i, j = 0, 0
    while i<m and j<n:
        # 若匹配，则指针后移，继续比较
        if target_str[i]==pattern_str[j]:
            i, j = i+1, j+1
        # 若遇到不匹配的字符，则将j重新置0，计算出本次开始比较的字符的下一个字符的索引
        else:
            i, j = i-j+1, 0
    # 得到匹配的字符串
    if j==n:
        return i-j  # 返回起始字符的索引
    return -1  # 无匹配，返回-1

if __name__ == "__main__":
    print(naive_matching("nice to meet you, lj", "meet"))

