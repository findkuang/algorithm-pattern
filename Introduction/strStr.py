#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 0015 22:44
# @Author  : kuangxiaojiang
# @Site    : 
# @File    : strStr.py
'''
注意：range(10),返回0-9
当循环结束时，中途没有返回，则可以直接返回return -1
leetcode地址: https://leetcode-cn.com/problems/implement-strstr/
'''


class Solution:
    def strStr(self, str1, str2):
        n, m =  len(str1), len(str2)
        for i in range(n-m+1):
            if str1[i:i+m] == str2:
                return i
        return -1

s = Solution()
str1 = 'abcde'
str2 = 'defd'
print(s.strStr(str1,str2))