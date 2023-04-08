#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 16:48
# @Author  : Aisonk
# @Function    : 排序数组中只出现一次的数字
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        异或运算
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res = res^num
        return res
