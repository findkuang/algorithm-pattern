#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 0001 21:34
# @Author  : Aisonk
# @Function    : 查找数组中第一个不重复的数字


def first_not_repetition_num(s_tr: str):
    """
    查找数组中第一个不重复的数字
    :param s_tr:
    :return:
    """
    list_str = []
    num = len(s_tr)
    for i in range(num):
        for j in range(num):
            if i == j and i != num-1:
                continue
            if s_tr[i] == s_tr[j] and i != num-1:
                break
            if j == num-1:
                list_str.append(s_tr[i])
    return list_str

s_tr = 'abcdacefmdbz'
print(first_not_repetition_num(s_tr))


def first_not_repetition_num_v2(s_tr: str):
    """
    查找数组中第一个不重复的数字
    :param s_tr:
    :return:
    """
    num = len(s_tr)
    had_repetition_list = []
    for i in range(num):
        for j in range(i+1, num):
            if s_tr[i] == s_tr[j] or s_tr[i] in had_repetition_list:
                had_repetition_list.append(s_tr[i])
                break
            if j == num - 1:
                return s_tr[i]
    return None
s_tr2 = 'abcdacefmdbz'
print(first_not_repetition_num_v2(s_tr2))