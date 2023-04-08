#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 0020 16:06
# @Author  : Aisonk
# @Function    :


def num_is_palindrome(num: int):
    if 10000 <= num < 100000:
        num = str(num)
        new_num = num[::-1]
        if num == new_num:
            return True
        else:
            return False
    else:
        message = '输入数据错误,请重新输入'
        return message


a = 12321
print(num_is_palindrome(a))