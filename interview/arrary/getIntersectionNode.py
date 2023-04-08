#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 0020 20:51
# @Author  : Aisonk
# @Function    : 判断两个链表是否相交
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        思路：先求出两个链表的差值，然后p1指针指向移动到差值位置，p1和p2同事移动，如果出现p1=p2,则出现相交
        """