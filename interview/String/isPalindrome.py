#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 0008 22:24
# @Author  : Aisonk
# @Function    : https://leetcode.cn/problems/valid-palindrome/


class Solution(object):
    def isPalindrome(self, s):
        """
        验证回文串
        :type s: str
        :rtype: bool
        """
        new_s = ''.join([zf for zf in s if zf.isalnum()]).lower()
        if new_s == "":
            return True
        num = len(new_s)
        left = 0
        right = num - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True

s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))