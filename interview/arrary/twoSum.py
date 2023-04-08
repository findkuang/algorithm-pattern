#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 10:36
# @Author  : Aisonk
# @Function    : 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = len(numbers)
        left = 0
        right = num - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return left, right

obj = Solution()
numbers = [1,2,4,6,10]
target = 10
print(obj.twoSum(numbers, target))