#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 11:11
# @Author  : Aisonk
# @Function    : 合并两个有序数组，不需要额外空间，从后往前遍历

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        只要m和n指针没遍历完就可以一直合并数组，如果m先遍历完，把nums2剩余元素直接赋值到nums1就行。
        """
        # 定义三个指针
        p1 = m - 1
        p2 = n - 1
        p1_all = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p1_all] = nums1[p1]
                p1 -= 1
                p1_all -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[p1_all] = nums2[p2]
                p2 -= 1
                p1_all -= 1
        # 如果p2 >=0, 则将nums2中剩下的追加到num1: 如果m先遍历完，把nums2剩余元素直接赋值到nums1就行
        if p2 >= 0:
            for i in range(p2 + 1):
                nums1[i] = nums2[i]
        return nums1
