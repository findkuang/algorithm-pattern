#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 0015 22:49
# @Author  : Aisonk
# @Function    : 区间合并
class Solution(object):
    def merge(self, intervals):
        """
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先以左区间值排序
        intervals.sort(key=lambda x: x[0])
        merge = []
        if len(intervals) <= 1:
            return intervals
        for i in range(1, len(intervals)):

            while intervals[i][0] <= intervals[i-1][1]:
                if not merge:
                    merge.append([intervals[i-1][0], intervals[i][1]])
                else:
                    pass

            else:
                merge.append(intervals[i])

