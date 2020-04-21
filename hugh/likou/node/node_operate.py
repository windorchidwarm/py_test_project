#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/17 14:47 
# @Author : Aries 
# @Site :  
# @File : node_operate.py 
# @Software: PyCharm

from hugh.likou.node.list_node import ListNode
from typing import List
from queue import PriorityQueue


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    start = head
    while n > 0:
        start = start.next
        n -= 1
    if n > 0: return head
    end = head
    if start is None:
        head = head.next
        return head
    while start.next is not None:
        start = start.next
        end = end.next
    end.next = end.next.next
    return head


def mergeKLists(lists: List[ListNode]) -> ListNode:
    '''
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
    :param self:
    :param lists:
    :return:
    '''
    if lists is None or len(lists) < 1:return

    head = point = ListNode(0)
    q = PriorityQueue()
    n = 0
    for l in lists:
        if l:
            q.put((l.val, n, l))
            n += 1
    while not q.empty():
        val, n, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, n, node))
            n += 1
    return head.next



if __name__ == '__main__':
    '''
    几点操作
    1->2->3->4->5 2
    '''
    head = ListNode(1)
    next = head
    for i in range(2, 6):
        node = ListNode(i)
        next.next = node
        next = node
    print(head)
    removeNthFromEnd(head, 2)

    lists = []
    head = ListNode(1)
    next = head
    for i in (4, 6):
        node = ListNode(i)
        next.next = node
        next = node
    lists.append(head)
    head = ListNode(2)
    next = head
    for i in (4, 5):
        node = ListNode(i)
        next.next = node
        next = node
    lists.append(head)
    head = ListNode(1)
    next = head
    for i in (3, 4):
        node = ListNode(i)
        next.next = node
        next = node
    lists.append(head)
    mergeKLists(lists)
