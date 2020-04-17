#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/17 14:47 
# @Author : Aries 
# @Site :  
# @File : node_operate.py 
# @Software: PyCharm

from hugh.likou.node.list_node import ListNode


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
