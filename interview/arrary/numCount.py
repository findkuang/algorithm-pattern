#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 0020 21:35
# @Author  : Aisonk
# @Function    : 统计有序数组中出现次数最多的元素
def get_max_count_num(nums):
    count_dict ={}
    max_count_num = None
    for num in nums:
        if not count_dict:
            max_count_num = num
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] = count_dict[num] + 1
            if count_dict[num] >= count_dict[max_count_num]:
                max_count_num = num
    return {max_count_num: count_dict[max_count_num]}

if __name__ == "__main__":
    nums = [1,1,2,2,3,4,5,5,5,6,8,8,8,8,9,10,11,11,11,11]
    print(get_max_count_num(nums))