#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
利用递归来求解背包问题

描述如下：
一个背包的总承载量为weight，现有n件物品的集合S，其中物品的重量分别为w_1,...w_n-1.
问题是能否从中选出若干件物品，其重量之和正好等于weight，如果存在就说明背包问题有解，否则，无解。
"""


def knap(weight, ob_list, n):
    """
    求出背包问题是否有解
    :param weight: 总承载量
    :param ob_list: 物品清单，存储的是各物品的质量
    :param n: 物品的件数
    :return: True 或 False
    """
    # 递归结束的条件1：正好用完所有的承载量
    if weight == 0:
        return True
    # 递归结束的条件2：承载量不够
    if weight < 0:
        return False
    # 递归结束的条件3：承载量过剩
    if weight > 0 and n < 1:
        return False
    # 若选择最后一件物品，则knap(weight, ob_list, n)是否有解，取决于knap(weight-ob_list[n-1],ob_list, n-1)是否有解
    if knap(weight-ob_list[n-1], ob_list, n-1):
        print("Item %s: %s" % (str(n-1), ob_list[n-1]))  # 打印出所选物品序号及其质量
        return True
    # 若不选择最后一件物品，则knap(weight, ob_list, n)是否有解，取决于knap(weight, ob_list, n-1)是否有解
    if knap(weight, ob_list, n-1):
        return True
    else:
        return False


if __name__ == '__main__':
    bag_weight = 30
    ob_list = [2, 2, 4, 6, 6, 10]
    n = len(ob_list)
    print(knap(bag_weight, ob_list, n))
