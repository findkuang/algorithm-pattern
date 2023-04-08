#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 0006 0:03
# @Author  : Aisonk
# @Function    :
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.backtrack(n, k, path, res, 1)
        return res

    def backtrack(self, n, k, path, res, start_index):
        if len(path) == k:
            # 注意：不能直接append(path), 此时的path是存放的引用地址
            res.append(path[:])
            return
        # 横向遍历
        for i in range(start_index, n+1):
            path.append(i)
            # 注意: 下一层递归的启示位置是i+1（纵向递归遍历）
            self.backtrack(n, k, path, res, i+1)
            path.pop()
s = Solution()
print(s.combine(4,2))