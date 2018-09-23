#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import deque


class Graph(object):
    """连通图类"""
    def __init__(self):
        self.node_neighbors = {}  # 邻接点
        self.visited_order = []  # 存储已经检查过的结点

    def nodes(self):
        return self.node_neighbors.keys()

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if (u != v):
                self.node_neighbors[v].append(u)

    # 深度优先遍历
    def depth_first_search(self, root=None):
        if root is not None:
            search_queue = deque()  # 队列
            search_queue.append(root)  # 入队

            visited = []
        else:
            print('root is None')
            return -1

        while search_queue:
            person = search_queue.popleft()  # 先进后出，相当于栈
            self.visited_order.append(person)

            if person not in visited and person in self.node_neighbors.keys():
                tmp = self.node_neighbors[person]
                tmp.reverse()

                for index in tmp:
                    search_queue.appendleft(index)

                visited.append(person)