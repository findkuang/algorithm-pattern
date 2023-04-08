#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 23:21
# @Author  : Aisonk
# @Function    : 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = int(x / 10)
        