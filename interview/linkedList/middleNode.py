#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 13:38
# @Author  : Aisonk
# @Function    :
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow