#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
单链表的实现
ADT list:  # 抽象数据类型
    List(self)  # 创建一个新表
    is_empty(self)  # 是否为空
    len(self)  # 长度
    prepend(self, elem)  # 将元素从头部插入
    append(self, elem)  # 将元素从尾部插入
    insert(self, elem. i)  # 将元素插入位置i
    del_first(self)  # 删除表中的首元素
    del_last(self)  # 删除尾元素
    del(self, i)  # 删除第i个元素
    search(self, elem)  # 查找元素elem在表中出现的位置，未出现返回-1
    for_all(self,op)  # 对表中每个元素执行操作op
"""


# 定义异常类(简单封装了ValueError，没有做修改)
class LinkedListUnderFlow(ValueError):
    pass


# 定义节点类
class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem  # 数据域
        self.next = next_  # 指向下一个节点


# 定义单链表类
class LList(object):
    def __init__(self):
        self._head = None  # 头指针

    def is_empty(self):
        """检查链表是否为空"""
        if self._head is None:
            return True
        return False

    def len(self):
        """计算链表的长度"""
        len_list = 0
        # 遍历单链表
        p = self._head
        while p is not None:
            len_list += 1
            p = p.next
        return len_list

    def prepend(self, elem):
        """头部插入元素"""
        self._head = LNode(elem, self._head)  # 与下面的两句等价
        # new_node = LNode(elem, self._head)
        # self._head = new_node

    def pop_first(self):
        """首端弹出元素"""
        # 先检查是否为空
        if self._head is None:
            raise LinkedListUnderFlow("in pop()")  # 引发溢出异常
        # 要弹出的元素
        e = self._head.elem
        self._head = self._head.next  # 将头指针指向下下一个元素（只有一个元素，则指向None，无需额外判断）
        return e

    def append(self, elem):
        """尾部插入元素"""
        # 原表如果为空，需要重新设置self._head指向新节点
        if self._head is None:
            self._head = LNode(elem)
            return
        # 遍历链表寻找尾端元素
        p = self._head
        while p.next is not None:
            p = p.next
        # 寻找到尾端元素为p
        # 插入操作只需要将p的next指向新节点
        p.next = LNode(elem)  # 新节点的next域默认为None

    def pop_last(self):
        """尾端弹出元素"""
        # 先检查是否为空
        if self._head is None:
            raise LinkedListUnderFlow("in pop()")  # 引发溢出异常
        # 遍历链表寻找尾端元素
        p = self._head
        # 如果表中只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        # 多个元素，遍历
        while p.next.next is not None:
            p = p.next
        # 找到最后一个元素为p.next(即p的下一个元素)
        # 弹出它，只需要将p设置为最后一个元素
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        """寻找特定的元素，满足pred(elem)为True"""
        p = self._head
        while p is None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def print_all(self):
        """打印链表中的元素"""
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')


if __name__ == '__main__':
    list_test = LList()
    list_test.prepend(1)
    list_test.append(9)
    list_test.append(10)
    list_test.print_all()
    print(list_test.pop_first())
    print(list_test.pop_last())
    list_test.print_all()
