#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 18:13
# @Author  : kuangxiaojiang
# @File    : preorderTraversal.py
# @Function: 二叉树前序非递归、中序非递归、后续非递归遍历
import collections


class Solution:
    def preorderTraversal(self, root):
        '''
        前序遍历非递归
        :param root:
        :return:
        '''
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
        '''
        中序遍历非递归
        :param root:
        :return:
        '''
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

    def inorderTraversal_two(self, root):
        '''
        中序遍历非递归第二种解法,
        先到左边根节点，然后再加入节点值，再访问有点节点
        :param root:
        :return:
        '''
        stack = []
        rst_list = []
        if root is None:
            return rst_list
        stack.append(root)
        node = stack.pop()
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node.left)
                node = node.left
            else:
                node = stack.pop()
                rst_list.append(node.value)
                node = node.right
        return rst_list

    def postorderTraversal(self, root):
        '''
        后续遍历非递归解法
        :param root:
        :return:
        '''
        pass

