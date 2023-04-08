#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 0015 23:08
# @Author  : kuangxiaojiang
# @Site    : 
# @File    : subsets.py

'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
'''
import copy


def the_whole_arrangement(choose_list):
    '''
    全排列回溯算法
    '''
    rst = []
    rst_list = []
    def backtrack(rst, choose_list):
        if len(rst) == 3:
            rst_list.append(rst[:])
            return
        for i in range(len(choose_list)):
            choose_list_new = copy.deepcopy(choose_list)
            choose_list_new.remove(choose_list[i])
            rst.append(choose_list[i])
            backtrack(rst, choose_list_new)
            rst.pop()
    backtrack(rst, choose_list)
    return rst_list


choose_list = [1,2,3]



def subsets(choose_list):
    '''
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）
    '''
    rst = []
    rst_list = []
    n = len(choose_list)
    def backtrack(start, k, rst=[]):
        if len(rst) == k:
            rst_list.append(rst[:])
            return
        for i in range(start, n):
            rst.append(choose_list[i])
            backtrack(i+1, k)
            rst.pop()
    for k in range(n+1):
        backtrack(0, k)
    return rst_list

print(subsets(choose_list))



