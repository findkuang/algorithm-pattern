#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 0003 15:53
# @Author  : Aisonk
# @Function    : 计算二叉树根节点到所有叶子节点的路径
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        path = []
        self.recursion(root, path, res)
        return res

    def recursion(self, node, path, res):
        # 递归终止条件
        if not node.left and not node.right:
            path.append(str(node.val))
            res.append('->'.join(path))
            return path
        path.append(str(node.val))
        if node.left:
            path = self.recursion(node.left, path, res)
            path.pop()
        if node.right:
            path = self.recursion(node.right, path, res)
            path.pop()
        return path
