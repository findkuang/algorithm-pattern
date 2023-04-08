#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/12 0012 11:34
# @Author  : Aisonk
# @Function    :  给定一个二叉树，找出其最小深度。
class Solution(object):
    def minDepth(self, root):
        """
        思路1：递归深度遍历
        思路2：使用层序遍历思路
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        quenue = [root]
        res = 0
        while quenue:
            # 每次遍历一层，当遇到为叶子节点时，则终止层序遍历
            res += 1
            size = len(quenue)
            for i in range(size):
                node = quenue[0]
                if node.left:
                    quenue.append(node.left)
                if node.right:
                    quenue.append(node.right)
                # 当node节点为叶子节点时，则终止循环
                if not node.left and not node.right:
                    quenue = []
                    break
                quenue.pop(0)
        return res
