#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 0010 18:29
# @Author  : Aisonk
# @Function    : 无重复字符的最长子串长度
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left = 0
        right = 0
        num = len(s)
        map = {}
        while left <= right and right < num:
            if s[right] not in map:
                map[s[right]] = right
                max_len = max(right-left+1, max_len)
                right += 1
            else:
                # 左指针挨个移动效率太低，用unordered_map来记录字符上一次出现的位置，如果出现过就把左指针移动到max(left, 字符上一次出现的位置+1)
                left = max(map[s[right]] + 1, left)
                map[s[right]] = right
                max_len = max(right - left + 1, max_len)
                right += 1

        return max_len