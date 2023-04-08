#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/12 0012 12:32
# @Author  : Aisonk
# @Function    : 删除一个字符串中所有出现的给定子字符串
class Solution(object):
    def removeOccurrences(self, s, part):
        """
        给你两个字符串 s 和 part ，请你对 s 反复执行以下操作直到 所有 子字符串 part 都被删除：
        模拟替换
        :type s: str
        :type part: str
        :rtype: str
        """
        part_len = len(part)
        if len(s) <= part_len and s != part:
            return s
        s_len = len(s)
        new_s = s
        i = 0
        while i < s_len:
            if i + part_len <= s_len:
                if new_s[i:i+part_len] == part:
                    # replace替换，如果指定第三个参数max，则替换不超过 max 次
                    new_s = new_s.replace(part, '', 1)
                    s_len = len(new_s)
                    i = 0
                else:
                    i += 1
            else:
                break
        return new_s
s = "aabababa"
part = "aba"
obj = Solution()
print(obj.removeOccurrences(s, part))
