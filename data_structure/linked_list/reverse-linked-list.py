#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/20 21:46
# @Author  : Aisonk
# @File    : reverse-linked-list.py
# @Function:

'''
反转一个单链表。
'''


def reverseList(head):
    if head is None:
        return head
    pt_slow = None
    pt_fast = head
    while pt_fast is not None:
        pt_temp = pt_fast.next
        pt_fast.next = pt_slow
        pt_slow = pt_fast
        pt_fast = pt_temp
    head = pt_slow
    return head


def reverseBetween(m, n, head):
    '''
    反转从位置  m  到  n  的链表。请使用一趟扫描完成反转。
    :param m:
    :param n:
    :param head:
    :return:
    '''