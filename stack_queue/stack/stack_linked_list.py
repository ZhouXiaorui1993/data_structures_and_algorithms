#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
基于链表技术实现栈，用LNode做节点
此时栈顶为链表首端元素
"""


# 定义自己的异常
class StackUnderFlow(ValueError):
    # 继承ValueError类
    pass


# 定义节点类
class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem  # 数据域
        self.next = next_  # 指向下一个节点


class LinkedStack(object):
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        """取出栈顶元素"""
        # 先检查是否为空
        if self._top is None:
            raise StackUnderFlow("in LinkedSatck.top()")
        # 非空，返回栈顶元素
        return self._top.elem

    def push(self, elem):
        """入栈"""
        self._top = LNode(elem, self._top)

    def pop(self):
        """出栈"""
        # 是否为空
        if self._top is None:
            raise StackUnderFlow("in LinkedList.pop()")
        # 非空，重置self._top，并返回出栈元素
        elem = self._top.elem
        self._top = self._top.next
        return elem


if __name__ == '__main__':
    stack_test = LinkedStack()
    for i in range(10):
        stack_test.push(i)

    print(stack_test.top())
    print(stack_test.pop())
    print(stack_test.top())
