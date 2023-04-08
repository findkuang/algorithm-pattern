#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 0020 20:27
# @Author  : Aisonk
# @Function    : 合并两个排序数组
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        双指针，前序遍历；需要额外的存储空间
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        sorted_list = []
        p1 = 0
        p2 = 0
        while(p1 < m and p2 < n):
            if nums1[p1] < nums2[p2]:
                sorted_list.append(nums1[p1])
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                sorted_list.append(nums2[p2])
                p2 += 1
            else:
                sorted_list.append(nums1[p1])
                sorted_list.append(nums2[p2])
                p1 += 1
                p2 += 1
        if p1 >= m and p2 <= n:
            sorted_list.extend(nums2[p2:])
        else:
            sorted_list.extend(nums1[p1:])
        nums1 = sorted_list[:]
        return nums1

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(s.merge(nums1, m, nums2, n))


