#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用栈解决一段文字中的括号匹配问题
"""

from stack_seqlist import *


def gen_parens(text):
    """括号生成器"""
    parens = '{}[]()'  # 所有会出现的括号形式
    len_txt = len(text)  # text的长度
    for i in range(len_txt):
        if text[i] in parens:
            yield text[i], i
            i += 1
        else:
            i += 1
    return


def check_parens(text):
    """检查括号是否匹配"""
    # 用字典存储匹配的括号，可用来查询
    paren_dict = {'{': '}', '(': ')', '[': ']'}

    # 开括号
    open_paren = '{[('

    paren_stack = MyStack()  # 用栈来存储text中的括号

    for p, i in gen_parens(text):
        # 若是开括号，则压入栈中
        if p in open_paren:
            paren_stack.push(p)
        else:
            # 若遇到闭括号
            # 检查是否和栈顶的开括号匹配，若匹配，则弹出栈顶元素，若不匹配，则抛出错误消息
            if not paren_stack.is_empty() and paren_dict[paren_stack.top()] == p:
                paren_stack.pop()
            else:
                print("unmatching is found at %s" % i)
                return
    print("all matching!")


if __name__ == '__main__':
    test_txt = "haha(zhou[xiao]ljsg{rui}([bendan]))"
    check_parens(test_txt)


