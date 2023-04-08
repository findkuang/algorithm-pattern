#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 0002 22:51
# @Author  : Aisonk
# @Function    : 二叉树层序遍历-广度遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            # 很重要：获取当前队列的长度，这个长度相当于 当前这一层的节点个数；遍历到此结束
            size = len(queue)
            level_nums = []
            for _ in range(size):
                level_nums.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
            res.append(level_nums)
        return res