#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 18:13
# @Author  : kuangxiaojiang
# @File    : preorderTraversal.py
# @Function: 二叉树前序非递归、中序非递归、后续非递归遍历
import collections


class Solution:
    def preorderTraversal(self, root):
        stack = []
        rst_list = []
        if root is None:
            return rst_list
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            rst_list.append(node.value)
            if not node.right:
                stack.append(node.right)
            if not node.left:
                stack.append(node.left)
        return rst_list

    def inorderTraversal(self, root):
        stack = []
        rst_list = []
        if root is None:
            return rst_list
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.right or node.left:
                if not node.right:
                    stack.append(node.right)
                stack.append(node.value)
                if not node.left:
                    stack.append(node.left)
            else:
                rst_list.append(node.value)

    def postorderTraversal(self, root):
        pass

