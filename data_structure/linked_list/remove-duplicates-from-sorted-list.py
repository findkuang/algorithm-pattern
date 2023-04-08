#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 16:49
# @Author  : Aisonk
# @File    : remove-duplicates-from-sorted-list.py
# @Function:

def deleteDuplicates(head):
    '''
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    :param head:
    :return:
    '''
    if head is None:
        return head
    pt1 = head
    pt2 = head.next
    while pt2 is not None:
        if pt1.value == pt2.value:
            pt2 = pt2.next
            pt1.next = pt2
        else:
            pt1 = pt2
            pt2 = pt2.next
    return head

