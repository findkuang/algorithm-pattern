#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/12 0012 18:13
# @Author  : Aisonk
# @Function    : 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre = head
        slow = None
        while pre:
            # 需要一个临时指针
            temp = pre.next
            pre.next = slow
            slow = pre
            pre = temp
        head = slow
        return head


