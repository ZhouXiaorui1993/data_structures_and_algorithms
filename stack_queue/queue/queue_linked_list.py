#!/usr/bin/env python3
# -*- coidng: utf-8 -*-

"""利用带有尾节点域的链表实现队列（保证首端（队首）弹出和尾端（队尾）插入时间复杂度都是O（1））

队列的抽象数据描述：

ADT Queue:
    Queue(self)   # 创建空的队列
    is_empty(self)   # 检查队列是否为空
    enqueue(self, elem)   # 将元素elem加入队列，称为入队
    dequeue(self)  # 删除队列内最早进入的元素，称为出队
    peek(self)  # 查看队列中最早入队的元素
"""


# 定义自己的异常
class QueueUnderFlow(ValueError):
    pass


# 定义节点类
class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem  # 数据域
        self.next = next_  # 指向下一个节点


class QueueLL(object):
    def __init__(self):
        self._head = None  # 链表的头节点
        self._rear = None  # 尾节点

    def is_empty(self):
        return self._head is None

    def enqueue(self, elem):  # 入队，从队尾入队，即尾端插入
        # 检查队列是否为空
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            new_node = LNode(elem)
            self._rear.next = new_node
            self._rear = new_node

    def dequeue(self):  # 出队，从队首弹出，即链表首端弹出
        # 检查队列是否为空
        if self._head is None:
            raise QueueUnderFlow("in dequeue().")
        else:
            e = self._head.elem
            self._head = self._head.next
            return e

    def peek(self):  # 察看队首的元素
        # 检查队列是否为空
        if self._head is None:
            raise QueueUnderFlow("in peek().")
        else:
            return self._head.elem

    def print_all(self):  # 打印队列中的元素
        p = self._head
        while p is not None:
            print(p.elem, end=' ')
            p = p.next
        print('\n')


if __name__ == '__main__':
    my_queue = QueueLL()
    my_queue.enqueue(10)
    my_queue.enqueue(12)
    my_queue.enqueue(13)
    my_queue.print_all()
    my_queue.dequeue()
    my_queue.print_all()
    print(my_queue.is_empty())
