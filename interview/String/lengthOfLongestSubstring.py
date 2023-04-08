#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 0010 11:42
# @Author  : Aisonk
# @Function    : 无重复字符的最长子串长度（set作为滑动窗口）
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        思路：  # 使用set作为滑动窗口，定义快慢指针
        :type s: str
        :rtype: int
        """
        # 使用set作为滑动窗口
        used_char = set()
        num = len(s)
        max_len = 0
        left = 0
        right = 0
        while left < num and right < num:
            if s[right] not in used_char:
                used_char.add(s[right])
                max_len = max(max_len, right-left+1)
                right += 1
            else:
                used_char.remove(s[left])
                left += 1
        return max_len

s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))