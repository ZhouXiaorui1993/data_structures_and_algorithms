#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
用list实现二叉树

每棵二叉树都用[d, l, tree]表示，分别表示节点数据、左子树和右子树
"""


class BinTree(object):
    def __init__(self, data=None):
        self.root = [data, None, None]

    def is_empty(self):
        return self.root == [None]*3

    def insert_left(self, new_branch):
        """在根结点和现有左子树中间插入新的左子树"""
        t = self.root.pop(1)  # 取出左子树
        self.root.insert(1, [new_branch, t, None])
    
    def insert_right(self, new_branch):
        t = self.root.pop(2)
        self.root.insert(2, [new_branch, None, t])
    
    def get_root_value(self):
        return self.root[0]
    
    def set_root_value(self, v):
        self.root[0] = v
    
    def get_left_tree(self):
        return self.root[1]
    
    def get_right_tree(self):
        return self.root[2]
    
    def show_tree(self):
        print(self.root)


if __name__ == '__main__':
    tree = BinTree(2)
    print(tree.is_empty())
    tree.insert_left(3)
    tree.insert_right(5)
    tree.insert_right(10)
    tree.show_tree()

    print(BinTree().is_empty())
