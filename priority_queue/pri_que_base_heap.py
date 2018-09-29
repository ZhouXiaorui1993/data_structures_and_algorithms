#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
基于堆实现优先队列，这里以最小堆为例
"""


class PriorityQueueError(ValueError):
    # 异常类
    pass


class PriorityQueue(object):
    def __init__(self, elist=[]):
        # 允许为优先队列传入一些初始元素
        self._elems = list(elist)
        if elist:
            # 如果有初始元素，则将这些元素做成一个堆
            self.build_heap()

    def is_empty(self):
        """判断是否为空"""
        return not self._elems

    def peek(self):
        """访问优先队列的队首元素"""
        if self.is_empty():
            raise PriorityQueueError("in peek")
        else:
            return self._elems[0]

    def enqueue(self, e):
        """元素e入队"""
        self._elems.append(None)  # 首先拓展顺序表
        # 注意这里并没有将元素存入再进行交换，而是"拿着它"去查找正确的插入位置
        self.shift_up(e, len(self._elems)-1)   # 向上筛选/上浮

    def dequeue(self):
        """队首元素出队"""
        if self.is_empty():
            raise PriorityQueueError("in dequeue")

        e0 = self._elems[0]  # 堆顶元素，真正要弹出堆的元素
        last_e = self._elems.pop()  # 取得末尾元素，并将其从顺序表弹出(这样弹出的复杂度为O(1))
        if len(self._elems) > 0:
            # 我们希望将last_e放到堆顶，然后进行下沉操作，重新将其做成一个堆
            # 这里和入队一样，先不进行交换，拿着last_e找到合适的位置，将其插入
            self.shift_down(last_e, 0, len(self._elems)-1)
        # 返回真正出列的元素
        return e0

    def build_heap(self):
        """将无序列表建成一个堆"""
        # 从右下结点开始，利用下沉方法，向左一个个建堆；
        # 然后再到上一层建堆（相当于给每两个子堆新增了堆顶，通过逐层下沉的方式构建新的大堆），直至整个表建成一个完整的堆
        end = len(self._elems)-1
        for i in range((end+1)//2, -1, -1):
            self.shift_down(self._elems[i], i, end)

    def shift_up(self, elem, last):
        """
        插入元素后，上浮操作
        :param elem: 待插入的元素
        :param last: 顺序表末尾的索引
        :return: 无
        """
        current_index = last  # 当前位于顺序表末尾
        current_parent_index = (current_index-1)//2   # 完全二叉树的性质，若子结点索引为i，则父结点的索引为(i-1)//2

        # 当结点上浮到根结点（索引为0）或找到elem>父结点_value时，退出循环，将结点插入
        while current_index > 0 and elem < self._elems[current_parent_index]:
            self._elems[current_index] = self._elems[current_parent_index]  # 将父结点放到当前结点的位置
            current_index = current_parent_index  # 上浮到父结点的位置
            current_parent_index = (current_index-1)//2  # 更新父结点的位置

        # 退出循环时，即找到了合适的插入位置，插入即可
        self._elems[current_index] = elem

    def shift_down(self, elem, begin, end):
        """
        弹出元素后，下沉操作
        :param elem: 操作的元素
        :param begin: 开始位置
        :param end: 结束位置，最多下沉到此位置
        :return: 无
        """
        current_index = begin
        current_son = current_index * 2 + 1  # 初始化为左子结点
        while current_son <= end:
            current_left = current_son
            current_right = current_left+1  # 右子结点的索引
            # 如果右结点存在且右结点较小
            if current_right <= end and self._elems[current_left] > self._elems[current_right]:
                current_son = current_right
            # 再将较小的子结点和elem比较
            # 如果elem较小，则可以退出循环了
            if elem <= self._elems[current_son]:
                break
            else:
                # 否则，将较小的子结点放入current索引
                self._elems[current_index] = self._elems[current_son]
                current_index = current_son
                current_son = current_index * 2 + 1

        # 退出循环时，已经找到了正确的位置，将其插入即可完成下沉
        self._elems[current_index] = elem

    def print_all(self):
        # 打印堆中的数据
        print(self._elems)


if __name__ == '__main__':
    test_pri_queue = PriorityQueue([1,4,6,2,3,5,0,7,-1])
    test_pri_queue.build_heap()
    test_pri_queue.print_all()

    test_pri_queue.enqueue(1)
    test_pri_queue.print_all()

    test_pri_queue.dequeue()
    test_pri_queue.print_all()







