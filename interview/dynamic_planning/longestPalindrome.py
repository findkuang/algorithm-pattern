#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 20:28
# @Author  : Aisonk
# @Function    : 最长回文子串-动态规划
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = len(s)
        begin = 0
        max_len = 1
        if num < 2:
            return s
        # 定义dp[i][j]表示以i为左,j为右的字符串是否为回文串
        # 定义二维动态数组
        dp = [[False]*num for _ in range(num)]
        # 初始化
        for i in range(num):
            dp[i][i] = True
        # 画二维矩阵表，确定遍历顺序 x轴表示右边界，y轴表示左边界
        for j in range(1, num):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 如果s[i] = s[j] 则子串是否回文串由dp[i+1][j-1]决定
                    if j-i < 3:
                        # 特殊情况，当长度为0或1时永远回文，则为回文串 j-1-(i+1)+1<2
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                # 获取最长回文子串
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin: begin+max_len]

obj = Solution()
s="babad"
print(obj.longestPalindrome(s))