#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/12 0012 9:50
# @Author  : Aisonk
# @Function    : 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        定义dp[i] 表示以nums[i]结尾的连续递增子序列
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [1 for _ in range(length)]
        # 初始化
        dp[0] = 1
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp)