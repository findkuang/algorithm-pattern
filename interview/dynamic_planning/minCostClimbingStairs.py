#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 0007 22:54
# @Author  : Aisonk
# @Function    : 使用最小花费爬楼梯-动态规划
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*(len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

s = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))