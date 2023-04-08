#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 0008 21:55
# @Author  : Aisonk
# @Function    : 最长递增子序列，思路
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        定义 dp[i] 表示以nums[i]结尾的最长递增子序列,
        则，如果nums[i] > [0,i]的一个数，则dp[i] = max(dp[i], dp[j]+1)
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [1 for _ in range(length)]
        # 初始化
        dp[0] = 1
        for i in range(1, length):
            # 从[0,i)中遍历，遍历过程中求最长递增子序列
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # 初始化dp[1]=1,每次遍历0~(i-1)的过程中，不断地取最大值做为dp[i]，保证最后dp[i]最大
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)