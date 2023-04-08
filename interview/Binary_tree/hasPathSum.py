#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 0003 19:50
# @Author  : Aisonk
# @Function    : 计算路径总和是否和targetNum相等
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        path_value = root.val
        if not root:
            return False
        res = self.digui(root, path_value, targetSum)
        return res

    def digui(self, node, path_value, targetSum):
        # 确定终止条件
        if path_value == targetSum and not node.left and node.right:
            return True
        left_flag, right_flag = False, False
        if node.left:
            path_value = path_value + node.left.val
            left_flag = self.digui(node.left, path_value, targetSum)
            path_value = path_value - node.left.val
        if node.right:
            path_value = path_value + node.right.val
            right_flag = self.digui(node.right, path_value, targetSum)
            path_value = path_value - node.right.val
        return left_flag or right_flag