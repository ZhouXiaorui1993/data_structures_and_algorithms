#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用非递归方式实现求阶乘的函数
"""

from stack_seqlist import *


def norec_fact(n):
    """求解n!"""
    # 定义一个栈，用于存储运算对象
    n_stack = MyStack()
    while n > 0:
        n_stack.push(n)
        n -= 1
    # 从栈中弹出一一运算
    res = 1
    while not n_stack.is_empty():
        res = res*n_stack.pop()
    return res


if __name__ == '__main__':
    print(norec_fact(4))
