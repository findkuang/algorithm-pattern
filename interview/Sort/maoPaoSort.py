#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 0003 22:23
# @Author  : Aisonk
# @Function    :


def maopao_sort(nums_data: list):
    """
    冒泡排序
    :param nums:
    :return:
    """
    length = len(nums_data)
    # 冒泡length-1轮
    for i in range(length-1):
        # 每轮冒泡length-i-1次
        for j in range(length-1-i):
            if nums_data[j+1] < nums_data[j]:
                nums_data[j], nums_data[j+1] = nums_data[j+1], nums_data[j]
    return nums_data

nums = [4,5,8,3,45,1,2,8,79,65,23,100]
print(maopao_sort(nums))
