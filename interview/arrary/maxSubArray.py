#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 22:24
# @Author  : Aisonk
# @Function    : 连续子数组的最大和

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        # dp[i] 定义为nums[i]结尾的最大子数组和
        # 初始化
        dp[0] = nums[0]
        # 遍历
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        # 返回以num[i]结尾的最大子数组和
        return max(dp)

obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(obj.maxSubArray(nums))