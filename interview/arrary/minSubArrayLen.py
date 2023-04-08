#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/1 0001 23:22
# @Author  : Aisonk
# @Function    : 求大于某个数值的最小子数组长度
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        思路： 双指针，滑动窗口机制
        """
        slow = 0
        fast = 0
        size = len(nums)
        # 无限大值
        res = float('inf')
        while fast <= size:
            if sum(nums[slow: fast]) >= target:
                need_nums = nums[slow: fast]
                print(need_nums)
                res = min(res, fast-slow)
                slow = slow + 1
            else:
                fast = fast + 1
        if res == float('inf'):
            return 0, []
        return res, need_nums

s = Solution()
nums = [2,3,1,2,4,3]
val = 7
print(s.minSubArrayLen(target=val, nums=nums))