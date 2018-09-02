#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
带有尾节点引用域（记录了尾节点所在的位置）的单链表，可以使得后端插入操作时间复杂度变为O(1),
但对于后端删除操作效率没有提升，因为删除后，需要找到倒数第二个节点，将rear指针指向它，这个过程的时间复杂度为O(n)
"""

from linked_list import *  # 导入普通的单链表类


class LListWithRear(LList):  # 继承之前的类
    def __init__(self):
        super(LListWithRear, self).__init__()
        self._rear = None  # 增加一个尾节点引用域

    # 考虑前端插入操作，加入新节点需要考虑尾节点引用域的设置，故重写prepend方法
    def prepend(self, elem):
        if self._head is None:  # 如果是空表，需要设置尾节点域
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):  # 后端插入
        if self._head is None:  # 如果是空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            new_node = LNode(elem)
            self._rear.next = new_node  # 当前尾节点的next域设置为新节点
            self._rear = new_node  # 设置新节点为尾节点

    def pop_last(self):  # 尾端弹出也会影响到尾节点域的设置
        if self._head is None:  # 如果是空表
            raise LinkedListUnderFlow("in pop_list")
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.elem  # 取得元素的数据域
            self._head = None  # 重置头节点为None
            self._rear = None  # 重置尾节点为None
            return e
        else:  # 表中元素大于1
            while p.next.next is not None:  # 直到p.next是尾节点，即找到倒数第二个节点
                p = p.next
            e = p.next.elem  # 尾节点的数据域，待返回的数据
            p.next = None  # 倒数第二个节点的next域设置为None
            self._rear = p  # 尾节点域指向倒数第二个节点
            return e


if __name__ == '__main__':
    list_test = LListWithRear()
    list_test.prepend(1)
    list_test.prepend(0)
    list_test.append(8)
    list_test.append(9)
    list_test.append(10)
    list_test.print_all()
    print(list_test.pop_first())
    print(list_test.pop_last())
    list_test.print_all()
