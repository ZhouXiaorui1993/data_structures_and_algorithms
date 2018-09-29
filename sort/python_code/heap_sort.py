#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""zhouxiaorui 2018/9/20
堆排序
"""


def heap_sort(e_list):
    """基于最大堆"""
    def shift_down(e_list, elem, begin, end):
        """
        下沉函数：将较小的元素下沉
        :param e_list: 待排序的列表
        :param elem:
        :param begin:
        :param end: 能沉到的极限位置，即堆底最后一个元素的位置
        :return:
        """
        current_index = begin  # elem当前所处的位置
        current_son = current_index*2+1  # elem所处位置的子结点位置，初始化为左孩子位置
        while(current_son <= end):  # 未沉到底，继续循环
            current_left = current_son
            current_right = current_left+1
            if current_right <= end and e_list[current_right] > e_list[current_left]:  # 当右孩子较大时
                current_son = current_right
            # 当elem最大时，表明最大的已经在上面了，没必要再下沉了
            if elem > e_list[current_son]:
                break
            # 否则，将较大的孩子放到current_index所指的结点上
            else:
                e_list[current_index] = e_list[current_son]
                # 更新current_index和current_son
                current_index = current_son
                current_son = 2*current_index + 1
        # 循环结束，找到了合适的位置
        e_list[current_index] = elem

    # 将e_list（视为一棵完全二叉树）中的元素逐层下沉，构建堆
    node_nums = len(e_list)
    for i in range(node_nums//2, -1, -1):
        shift_down(e_list, e_list[i], i, node_nums-1)

    print(e_list)

    # 开始排序，每次将堆顶元素取出放到列表末尾，将末尾元素从堆顶开始下沉
    len_elist = len(e_list)
    for i in range(len_elist-1, 0, -1):
        max_elem = e_list[0]
        end_elem = e_list[i]
        e_list[i] = max_elem
        # 将第i个元素下沉
        shift_down(e_list, end_elem, 0, i-1)

    print("after sort:\n %s" % e_list)


if __name__ == '__main__':
    a = [2,12,4,5,1,7,7,0,34,24,13,6]
    heap_sort(a)