#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 0006 11:39
# @Author  : Aisonk
# @Function    :
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        total = 0
        self.trackback(k, n, path, total, res, 1)
        return res

    def trackback(self, k, n, path, total, res, start_index):
        if len(path) == k:
            if total == n:
                res.append(path[:])
            return
        for i in range(start_index, 10):
            path.append(i)
            total = total + i
            self.trackback(k, n, path, total, res, i+1)
            total = total - i
            path.pop()

s = Solution()
print(s.combinationSum3(2,9))