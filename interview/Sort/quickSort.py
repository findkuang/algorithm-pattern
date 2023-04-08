#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 0003 22:43
# @Author  : Aisonk
# @Function    : 快速排序,算法


def quick_sort_recursion(nums: list, left, right):
    """
    快速排序递归, 以left=begin作为基准数据，从右侧开始出发，right找出小于基数的值，left找出大于基数的值，然后再交换两个数值
    :param nums:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        return
    jishu_num = nums[left]
    # 需要用begin,i,j保存变量；如果直接使用left,right则会修改right的值，导致右侧排序的参数错误。
    begin = left
    # 设置左指针
    i = left
    # 设置右指针
    j = right
    while i < j:
        # 注意：一定要从最右侧开始出发
        while i < j and nums[j] > jishu_num:
            j -= 1
        while i < j and nums[i] <= jishu_num:
            i += 1
        # 交换顺序
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # 当left和right相遇后，需要把同时指向的数据和基准数据对换(如果以右侧开始滑动时，则当左右指针相遇时，指针所指向的值一定比基数小)
    nums[begin], nums[i] = nums[i], nums[begin]
    # 左侧排序
    quick_sort_recursion(nums, begin, i-1)
    # 右侧排序
    quick_sort_recursion(nums, i+1, right)
    return nums

nums = [12,45,79,1,12,5,8,6,7,44]
print(quick_sort_recursion(nums, 0, len(nums)-1))