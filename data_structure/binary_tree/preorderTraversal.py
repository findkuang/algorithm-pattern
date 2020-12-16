#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 18:13
# @Author  : kuangxiaojiang
# @File    : preorderTraversal.py
# @Function: 前序非递归
import collections

class Solution:
    def preorderTraversal(self, root):
        stack = []
        rst_list = []
        if root is None:
            return rst_list
        stack.append(root)
        node = stack[:-1]
        while len(stack) > 0:
            if not node.left:
                stack.append(node.left)
            if not node.right:
                stack.append(node.right)

