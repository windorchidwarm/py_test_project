#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : num_list_node.py
# Author: chen
# Date  : 2020-05-04

from hugh.likou.node.list_node import ListNode

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1: return l2
    if not l2: return l1

    head = None
    l1_tmp = l1
    l2_tmp = l2
    tmp = None
    add_nums = 0
    while l1_tmp and l2_tmp:
        num = l1_tmp.val + l2_tmp.val + add_nums
        if num > 9:
            num = num % 10
            add_nums = 1
        else:
            add_nums = 0

        if tmp:
            tmp.next = ListNode(num)
            tmp = tmp.next
        else:
            head = ListNode(num)
            tmp = head
        l1_tmp = l1_tmp.next
        l2_tmp = l2_tmp.next
    if l1_tmp:
        while add_nums > 0 and l1_tmp:
            num = l1_tmp.val + add_nums
            if num > 9:
                num = num % 10
                add_nums = 1
            else:
                add_nums = 0
            tmp.next = ListNode(num)
            tmp = tmp.next
            l1_tmp = l1_tmp.next
        tmp.next = l1_tmp
    if l2_tmp:
        while add_nums > 0 and l2_tmp:
            num = l2_tmp.val + add_nums
            if num > 9:
                num = num % 10
                add_nums = 1
            else:
                add_nums = 0
            tmp.next = ListNode(num)
            l2_tmp = l2_tmp.next
            tmp = tmp.next
        tmp.next = l2_tmp
    if add_nums > 0:
        tmp.next = ListNode(add_nums)
    return head