#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
利用list(顺序表)封装一个自己的栈类
"""


# 定义自己的异常
class StackUnderFlow(ValueError):
    # 继承ValueError类
    pass


class MyStack(object):
    def __init__(self):
        self._elem = []  # 用list存储栈中的元素

    def is_empty(self):
        """判断栈是否为空"""
        return self._elem == []

    def top(self):
        if len(self._elem) == 0:
            raise StackUnderFlow("in MyStack.top()")
        else:
            return self._elem[-1]

    def push(self, elem):
        """将元素压入栈中"""
        self._elem.append(elem)

    def pop(self):
        if len(self._elem) == 0:
            raise StackUnderFlow("in MyStack.pop()")
        return self._elem.pop()


if __name__ == '__main__':
    stack_test = MyStack()
    stack_test.push(1)
    stack_test.push(4)
    print(stack_test.top())
    print(stack_test.pop())
    print(stack_test.top())
    # stack_test.pop()

