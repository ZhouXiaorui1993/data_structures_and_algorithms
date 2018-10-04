#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉搜索树各种方法的实现
"""


class BinTreeNode(object):
    """结点类"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinSearchTree(object):
    """二叉搜索树"""
    def __init__(self, root_node=None):
        self._root = root_node

    # 检查是否为空
    def is_empty(self):
        return self._root is None

    # 在BST中搜素某个数
    def search(self, key):
        r_node = self._root
        while r_node is not None:
            entry = r_node.data
            if key < entry:
                r_node = r_node.left
            elif key > entry:
                r_node = r_node.right
            else:
                return entry
    
        return None  # 检索失败
    
    # 插入数据
    # 不仅需要保证二叉树的结构完整，将新的数据加入到树中，还需要保证树中结点数据的正确顺序
    # 关键在于找到加入新结点的正确位置，并将新结点正确链接到树中
    def insert(self, key):
        r_node = self._root
        if r_node is None:
            self._root = BinTreeNode(key)
            return 
        while True:
            entry = r_node.data
            if key < entry:  # key较小，插入到左子树
                if r_node.left is None:
                    r_node.left = BinTreeNode(key)  # 遇到为空，则插入
                    return
                else:  # 否则，继续去下面的左子树中寻找位置
                    r_node = r_node.left
            elif key > entry:  # key较大，插入到右子树
                if r_node.right is None:
                    r_node.right = BinTreeNode(key)
                    return
                else:  # 否则，继续去下面的右子树中寻找位置
                    r_node = r_node.right
            else:  # 如果遇到key相同的数据，则替换该数据
                r_node.data = key
                return

    # 定义一个迭代器，使得用户可以取得其中的所有数据
    # 中序遍历，对于BST而言，其他类型的遍历意义不大
    def get_values(self):
        current_node = self._root
        stack = list()
        while current_node is not None or stack:
            while current_node is not None:  # 将所有的左结点压入栈中
                stack.append(current_node)  # 将当前结点压入栈中
                current_node = current_node.left  # 设置当前结点为其左结点
            current_node = stack.pop()
            yield current_node.data
            current_node = current_node.right

    def get_root(self):
        return self._root


def find_closest(root_node, target_n):
    """查找树中与n最接近的结点"""
    # 如果根结点为空或根结点中的数据等于n，则返回根结点
    if root_node is None or root_node.data == target_n:
        return root_node
    # 如果比根结点大，则在右子树中查找
    if target_n > root_node.data:
        if root_node.right is None:
            return root_node
        else:
            left_nearest = find_closest(root_node.right, target_n)
            if abs(left_nearest.data-target_n) < abs(root_node.data-target_n):
                return left_nearest
            else:
                return root_node
    # 如果比根结点小，则在左子树中查找
    if target_n < root_node.data:
        if root_node.left is None:
            return root_node
        else:
            right_nearest = find_closest(root_node.left, target_n)
            if abs(right_nearest.data-target_n) < abs(root_node.data-target_n):
                return right_nearest
            else:
                return root_node


if __name__ == '__main__':
    bst_test = BinSearchTree()
    bst_test.insert(3)
    bst_test.insert(23)
    bst_test.insert(12)
    bst_test.insert(1)
    bst_test.insert(7)
    bst_test.insert(10)
    # 中序遍历
    for i in bst_test.get_values():
        print(i)
    # 查找最接近的target_num的结点
    target_num = 6
    closest_node = find_closest(bst_test.get_root(), target_num)
    print("the closest node is %s" % closest_node.data)
