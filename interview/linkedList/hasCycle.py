#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 0009 11:54
# @Author  : Aisonk
# @Function    : 给你一个链表的头节点 head ，判断链表中是否有环, 并找出环的位置。

class Solution(object):
    def hasCycle(self, head):
        """
        从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点。
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = head
        # p2和p2.next都需要判空验证
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                # 从head节点，相遇节点同时步调出发，在环形入口相交
                index1 = head
                index2 = p2
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return True, index1
        return None