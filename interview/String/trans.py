#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 0015 22:35
# @Author  : Aisonk
# @Function    :
class Solution:
    def trans(self, s: str, n):
        """
        字符串变形：
        对于一个长度为 n 字符串，我们需要对它做一些变形。
        首先这个字符串中包含着一些空格，就像"Hello World"一样，然后我们要做的是把这个字符串中由空格隔开的单词反序，同时反转每个字符的大小写。
        比如"Hello World"变形后就变成了"wORLD hELLO"。
        :param s:
        :param n:
        :return:
        """
        s = s.swapcase()
        s_list = s.split(' ')
        news = ' '.join(s_list[::-1])
        return news