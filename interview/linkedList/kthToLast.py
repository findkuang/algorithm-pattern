#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 13:52
# @Author  : Aisonk
# @Function    : 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        slow = head
        fast = head
        # 首先，快指针向前移动k个位置
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val