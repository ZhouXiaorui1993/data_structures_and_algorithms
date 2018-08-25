#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
利用栈结构来计算后缀表达式

后缀表达式：
例如: 3 5 - 6 17 4 * + * 3 /
写成中缀表达式为：(3-5)*(6+17*4)/3
"""

from stack_seqlist import *


class SStack(MyStack):
    """
    继承原栈，并在此基础上添加一个计算栈深度的方法
    """
    def depth(self):
        return len(self._elem)


def calc_pos_exp(exp_lst):
    """表达式用list形式传入"""
    # 操作符
    operator = "+-*/"
    # 初始化一个栈
    exp_stack = SStack()

    # 将表达式字符顺序压入栈中
    for i in exp_lst:
        # 若非操作符，则入栈
        if i not in operator:
            exp_stack.push(i)
        # 若是操作符，弹出栈顶的两个元素进行计算，得到的结果压入栈中
        else:
            a = float(exp_stack.pop())
            b = float(exp_stack.pop())
            if i == '+':
                m_res = b+a
            elif i == '-':
                m_res = b-a
            elif i == '*':
                m_res = b*a
            elif i == '/':
                m_res = b/a
            exp_stack.push(str(m_res))
    # 遍历结束，检查栈中是否只有一个元素，如果是，证明运算结束
    if exp_stack.depth() == 1:
        return exp_stack.pop()
    else:  # 否则，证明有多余的运算符
        raise SyntaxError("多余的运算符")


if __name__ == '__main__':
    # test_exp = [3, 5, '-', 6, 17, 4, '*', '+', '*', 3, '/']
    test_exp = '3 5 - 6 17 4 * + * 3 /'
    test_exp = test_exp.split(' ')
    print(calc_pos_exp(test_exp))



