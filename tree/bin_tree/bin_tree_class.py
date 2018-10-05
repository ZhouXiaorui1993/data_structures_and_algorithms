#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""二叉树的类实现，以及遍历等各种方法"""


# 结点类
class BinTreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left  # 左子树
        self.right = right  # 右子树

# 统计树中结点的个数
def count_bintree_nodes(node: BinTreeNode):
    # 递归实现
    if node is None:
        return 0
    return 1+count_bintree_nodes(node.left)+count_bintree_nodes(node.right)


# 计算树中结点的数据和
def sum_tree_nodes(node: BinTreeNode):
    # 递归实现
    if node is None:
        return 0
    else:
        return node.val + sum_tree_nodes(node.left) + sum_tree_nodes(node.right)


# 遍历算法
# 递归实现——前序遍历
def preorder_dfs_rec(root:BinTreeNode, proc=print):
    if root is None:
       return
    cur_node = root
    proc(cur_node.val)
    if root.left is not None:
        preorder_dfs_rec(cur_node.left)
    if root.right is not None:
        preorder_dfs_rec(cur_node.right)


# 非递归实现——前序遍历
def preorder_dfs(root: BinTreeNode, proc=print):
    cur_node = root
    stack = list()  # 用栈来实现

    while cur_node is not None or stack:  # 栈不为空
        # 先处理左子树，直到左结点处理结束
        while cur_node is not None:
            proc(cur_node.val)   # 先处理父结点
            stack.append(cur_node)
            cur_node = cur_node.left
        if stack:  # 此时栈顶结点是处理过的父结点
            cur_node = stack.pop()
            cur_node = cur_node.right  # 当前结点设置为右子结点


# 递归实现——中序遍历
def midorder_dfs_rec(root:BinTreeNode, proc=print):
    if root is None:
        return
    # 先处理左子树
    if root.left:
        midorder_dfs_rec(root.left)
    # 处理根结点
    proc(root.val)
    # 再处理右子树
    if root.right:
        midorder_dfs_rec(root.right)


# 非递归实现——中序遍历
def midorder_dfs(root:BinTreeNode, proc=print):
    stack = list()
    cur_node = root
    while cur_node is not None or stack:  # 当cur_node为None且栈为空时，退出循环
        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        # 左孩子为空了，stack不为空
        if stack:
            cur_node = stack.pop()
            proc(cur_node.val)
            cur_node = cur_node.right

# 递归实现，后序遍历
def lastorder_dfs_rec(root:BinTreeNode, proc=print):
    if root is None:
        return
    # 左子树
    lastorder_dfs_rec(root.left)
    # 右子树
    lastorder_dfs_rec(root.right)
    # 根结点
    proc(root.val)


# 非递归实现，后序遍历
def lastorder_dfs(root:BinTreeNode, proc=print):
    stack = list()
    cur_node = root
    while cur_node is not None or stack:
        while cur_node is not None:  # 下行循环，直到栈顶的两子树为空
            stack.append(cur_node)
            if cur_node.left is not None:  # 能左就左，否则向右一步
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        # 入栈操作结束，两子树为空，cur_node=None
        cur_node = stack.pop()  # 栈顶是应该访问的结点
        proc(cur_node.val)
        if stack and stack[-1].left == cur_node:  # 栈不为空，且当前结点是栈顶的左子结点
            cur_node = stack[-1].right  # 当前结点向右一步
        else:
            cur_node = None  # 没有右子树或者右子树遍历完毕，则强迫退栈



if __name__ == '__main__':
    bin_tree = BinTreeNode(2, BinTreeNode(3, BinTreeNode(4), BinTreeNode(6)), BinTreeNode(5, BinTreeNode(10), BinTreeNode(12)))
    print("树中的总结点数量：%s" % count_bintree_nodes(bin_tree))
    print("树中结点数据总和：%s" % sum_tree_nodes(bin_tree))

    print("递归实现，前序遍历序列：")
    preorder_dfs_rec(bin_tree)

    print("非递归实现，前序遍历序列：")
    preorder_dfs(bin_tree)

    print("递归实现，中序遍历序列：")
    midorder_dfs_rec(bin_tree)

    print("非递归实现，中序遍历序列：")
    midorder_dfs(bin_tree)

    print("递归实现，后序遍历序列：")
    lastorder_dfs_rec(bin_tree)

    print("非递归实现，后序遍历序列：")
    lastorder_dfs(bin_tree)