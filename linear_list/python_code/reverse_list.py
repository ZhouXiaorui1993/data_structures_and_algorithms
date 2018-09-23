#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
链表反转的实现

方法1：利用三个指针遍历单链表，逐个结点进行反转
方法2：从第2个节点到第N个节点，依次逐节点插入到第1个节点(head节点)之后，最后将第一个节点挪到新表的表尾。
"""

from linked_list import *  # 导入单链表类


def reverse_link_list1(link_list: LList):  # 用冒号注明，可表示期望的数据类型，但即便输入的不是该类型的数据，解释器依然不会报错
    """利用三个指针来反转单链表"""
    head = link_list._head  # 头结点
    p = head
    q = p.next
    head.next = None  # 将头结点的next域改为None
    while q is not None:
        r = q.next
        q.next = p
        p = q
        q = r
    # 循环结束，q是None，p是尾结点
    # 将原来的尾结点设置为首结点
    link_list._head = p

    link_list.print_all()


def reverse_link_list2(link_list: LList):
    pass


if __name__ == "__main__":
    # reverse_link_list1("2")
    test_list = LList()
    test_list.prepend(1)
    test_list.append(2)
    test_list.prepend(0)
    test_list.append(3)
    # print(test_list._head)
    test_list.print_all()

    reverse_link_list1(test_list)