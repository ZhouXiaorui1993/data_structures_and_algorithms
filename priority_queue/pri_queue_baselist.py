#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""基于list实现优先队列"""


class PrioQueueError(ValueError):
    # 异常类
    pass


# 优先队列类
class PrioQue(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)  # 初始elist可以是任何可迭代对象
        self._elems.sort(reverse=True)  # 倒序排序，这里假设最小的参数优先级最高

    def enqueue(self, e):  # 入队，需要找到合适的插入位置
        i = len(self._elems) - 1
        while i >= 0:
            if e > self._elems[i]:  # 从队尾开始比较，如果较大，则前移
                i -= 1
            else:
                break

        self._elems.insert(i+1, e)  # insert的索引可以比list中最大索引大，此时会插入到最后

    def is_empty(self):
        return not self._elems

    def peek(self):  # 访问优先级最高的元素
        if self.is_empty():
            raise PrioQueueError("in top")

        else:
            return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        else:
            return self._elems.pop()


if __name__ == '__main__':
    priority_queue = PrioQue([12, 6, 23, 2, 9])
    print(priority_queue.peek())
    priority_queue.enqueue(8)
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())
    print(priority_queue.dequeue())