#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 16:49
# @Author  : kuangxiaojiang
# @File    : balanced-binary-tree.py
# @Function:
'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
'''


class Solution:
    def isBalanced(self, root):
        '''
        思路 1：分治法，左边平衡 && 右边平衡 && 左右两边高度 <= 1，
        计算每一个节点是否平衡；如果所有节点平衡，则改树为平衡二叉树
        :param root:
        :return:
        '''
        def depth(root):
            if root is None:
                return 0, True
            else:
                l_depth, rst_l = depth(root.left)
                r_depth, rst_r = depth(root.left)
                return max(l_depth, r_depth)+1, rst_l and rst_r and (abs(l_depth-r_depth)<=1)

