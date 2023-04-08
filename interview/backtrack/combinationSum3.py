#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 0006 11:30
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
        self.trackback(k, n, path, res, 1)
        return res

    def trackback(self, k, n, path, res, start_index):
        if len(path) == k and sum(path) == n:
            res.append(path[:])
            return
        for i in range(start_index, 10):
            path.append(i)
            self.trackback(k, n, path, res, i+1)
            path.pop()

s = Solution()
print(s.combinationSum3(3,9))