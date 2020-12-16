#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 16:15
# @Author  : kuangxiaojiang
# @File    : maximum-depth-of-binary-tree.py
# @Function:
'''
给定一个二叉树，找出其最大深度。
递归
'''
import collections

# 1.递归
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            return depth


# 2.层序遍历方法
class Solution_A:
    def maxDepth(self, root):
        if root is None:
            return 0
        bfs = collections.deque([root])
        depth = 0
        pass


#3. 二叉树层序遍历
class Solution_B:
    def levelOrder(self, root):
        rst = []
        if root is None:
            return rst
        bfs = collections.deque([root])
        while len(bfs) > 0:
            node = bfs.popleft()
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
            rst.append(node.value)
        return rst

