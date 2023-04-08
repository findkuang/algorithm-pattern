#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/1 0001 17:31
# @Author  : Aisonk
# @Function    :
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        k = 0
        for i in range(size):
            index = i
            if nums[index] == val:
                for j in range(i+1, size):
                    nums[j-1] = nums[j]
                index = i -1
                k = k -1
                nums[k] = None
        return size+k, nums

s = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums, 2))