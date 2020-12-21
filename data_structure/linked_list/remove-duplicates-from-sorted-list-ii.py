#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 19:00
# @Author  : Aisonk
# @File    : remove-duplicates-from-sorted-list-ii.py
# @Function:
'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中   没有重复出现的数字。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if head is None:
        return head
    head_copy = ListNode(next=head)
    pt_slow = head
    pt_fast = pt_slow.next
    while pt_fast is not None:
        if pt_fast.next != pt_slow.next:
            pt_slow = pt_slow.next
            pt_fast = pt_fast.next
        else:
            pt_fast = pt_fast.next
        if pt_slow == head:
            head_copy = pt_fast
            head = head_copy
        else:
            pt_slow.next = pt_fast
    return head




