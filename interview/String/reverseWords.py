#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 0003 20:29
# @Author  : Aisonk
# @Function    :


def reverse_str(data: str):
    """
    针对所有字符串的操作处理，需要先转换为list后，才能替换修改值。str类型本身是不能修改值的
    字符串反转，原有单词顺序不变
    :param words:
    :return:
    """
    # 切记：对字符穿的替换操作，必须先转为list;才能交换处理
    data = list(data)
    right = len(data) - 1
    reverse_word(data, 0, right)
    slow = 0
    fast = 0
    while fast < len(data):
        if data[slow] == '#':
            slow += 1
            fast += 1
        if data[fast] != '#':
            fast += 1
        else:
            reverse_word(data, slow, fast-1)
            slow = fast
    # 最后一组需要再反转，因为末尾没有以#结尾。
    reverse_word(data, slow, fast-1)
    return ''.join(data)


def reverse_word(word: list, left, right):
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1


data = 'abcd####def###ghe##'
print(reverse_str(data))