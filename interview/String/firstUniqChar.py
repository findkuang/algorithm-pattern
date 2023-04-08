#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 0008 22:57
# @Author  : Aisonk
# @Function    : https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/

class Solution(object):
    def firstUniqChar(self, s):
        """
        获取字符串中第一个只出现一次的字符
        :type s: str
        :rtype: str
        """
        count_map = {}
        for char in s:
            if char not in count_map:
                count_map[char] = 1
            else:
                count_map[char] += 1
        for char in s:
            if count_map[char] == 1:
                return char
        return " "