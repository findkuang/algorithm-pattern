#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 0010 15:59
# @Author  : Aisonk
# @Function    :
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle
        return -1