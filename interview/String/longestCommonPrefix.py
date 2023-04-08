#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 0015 21:21
# @Author  : Aisonk
# @Function    : 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 获取最短的字符串，然后再遍历判断
        min_str_len = float('inf')
        common_str = ''
        stop = False
        for i in range(len(strs)):
            if len(strs[i]) < min_str_len:
                min_str = strs[i]
                min_str_len = len(strs[i])
        if not min_str:
            return common_str
        for j in range(len(min_str)):
            for str in strs:
                if min_str[j] != str[j]:
                    stop = True
                    break
            if not stop:
                common_str += min_str[j]
        return common_str




