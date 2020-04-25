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


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    '''
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
    示例：
    给你这个链表：1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5
    :param head:
    :param k:
    :return:
    '''
    if not head or not head.next:
        return head
    else:
        tmp_node = head
        node_list = []
        i = 0
        while i < k and tmp_node:
            node_list.append(tmp_node)
            tmp_node = tmp_node.next
            i += 1
        head_node =node_list[-1]
        head_tmp = node_list[-1]
        m = len(node_list)
        for j in range(2, m + 1):
            head_tmp.next = node_list[-j]
            head_tmp = head_tmp.next
        pre_head = head_tmp

        while tmp_node:
            i = 0
            node_list.clear()
            while i < k and tmp_node:
                node_list.append(tmp_node)
                tmp_node = tmp_node.next
                i += 1
            m = len(node_list)
            if m == k:
                head_tmp = node_list[-1]
                pre_head.next = head_tmp

                for j in range(2, m + 1):
                    head_tmp.next = node_list[-j]
                    head_tmp = head_tmp.next
                head_tmp.next = tmp_node
                pre_head = head_tmp
            else:
                pre_head.next = node_list[0]
        return head_node


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def reverse(head_node):
        pre = None
        cur = head_node
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    end = dummy
    while end:
        i = 0
        while i < k and end:
            end = end.next
            i += 1
        if not end: break
        start = pre.next
        next_node = end.next
        end.next = None
        pre.next = reverse(start)
        start.next = next_node
        pre = start
        end = pre

    return dummy.next

def swapPairs(head: ListNode) -> ListNode:
    '''
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    :param self:
    :param head:
    :return:
    '''
    if head is None or head.next is None:
        return head
    else:
        first = head
        head = head.next

        last = first.next
        first.next = last.next
        last.next = first
        pre = first
        first = first.next

        while first is not None and first.next is not None:
            last = first.next
            first.next = first.next.next
            last.next = first
            pre.next = last

            pre = first
            first = first.next
        return head

def swapPairs2(head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


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
