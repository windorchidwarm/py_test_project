#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/19 11:07 
# @Author : Aries 
# @Site :  
# @File : list_list.py 
# @Software: PyCharm

class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data


def remove_nth_from_end(list_node, n):
    dump = ListNode(0)
    dump.next = list_node
    first = dump
    second = dump

    for num in range(n + 1):
        first = first.next

    while first is not None:
        first = first.next
        second = second.next

    print(second.next.get_data())
    second.next = second.next.next
    return dump.next


def two_sum(nums, target):
    if nums is None or len(nums) < 2:
        return 0,0

    num_map = {}
    for idx in range(len(nums)):
        if nums[idx] in num_map:
            return num_map[nums[idx]], idx
        else:
            num_map[target - nums[idx]] = idx
    return 0,0


def is_loop(list_node):
    node1 = list_node
    node2 = list_node
    ret = False
    while node2.next is not None and node2.next.next is not None:
        node1 = node1.next
        node2 = node2.next.next

        if node1 == node2:
            ret = True
            break
    return ret



def is_no_loop_join(node1, node2):
    p1 = node1
    p2 = node2

    while p1.next is not None:
        p1 = p1.next

    while p2.next is not None:
        p2 = p2.next

    return p1 == p2



def fib(n):
    a = []

    for j in range(n):
        a.append(0)

    a[0] = 1
    a[1] = 1

    for j in range(2, n):
        a[j] = a[j - 1] + a[j -2]
    return a[n - 1]



def n_multiplication(n):
    a = []
    for j in range(n):
        a.append(0)

    a[0] = 1

    for j in range(1, n):
        a[j] = a[j - 1] * (j + 1)

    return a[n - 1]


def edit_path(s1, s2):
    def dp(i, j):
        if i == -1: return j + 1
        if j == -1: return i + 1

        if s1[i] == s2[j]:
            return dp(i - 1, j - 1)
        else:
            return min(dp(i, j - 1) + 1,  # 插入
                       dp(i - 1, j) + 1, # 删除
                       dp(i - 1, j - 1) + 1) # 替换
    return dp(len(s1) - 1, len(s2) - 1)



def min_edit_path(s1, s2):
    memo = dict()

    def dep_min(c, d) -> int:
        if (c, d) in memo:
            return memo[(c, d)]

        if c == -1:
            return d + 1
        if d == -1:
            return c + 1

        if s1[c] == s2[d]:
            memo[(c, d)] = dep_min(c - 1, d - 1)
        else:
            memo[(c, d)] = min(dep_min(c, d - 1) + 1, dep_min(c - 1, d) + 1, dep_min(c - 1, d - 1) + 1)
        return memo[(c, d)]
    return dep_min(len(s1) - 1, len(s2) - 1)


def min_edit_path_2(s1, s2):
    m_path = [[-1 for d in range(len(s2) + 1)]] * (len(s1) + 1 )
    for a in range(len(s1)):
        m_path[a][0] = a

    for b in range(len(s2)):
        m_path[0][b] = b

    for a in range(1, len(s1) + 1):
        for b in range(1, len(s2) + 1):
            if s1[a - 1] == s2[b - 1]:
                m_path[a][b] = m_path[a - 1][b - 1]
            else:
                m_path[a][b] = min(m_path[a][b - 1], m_path[a - 1][b], m_path[a - 1][b - 1]) + 1
    return m_path[len(s1)][len(s2)]


if __name__ == '__main__':
    print('------------')
    list_node = ListNode(12)
    range_node = list_node
    for i in range(99):
        range_node.next = ListNode(i)
        range_node = range_node.next

    print(remove_nth_from_end(list_node, 3).get_data())
    print(fib(5))
    print(n_multiplication(4))
    print(edit_path('horse', 'ros'))
    print(min_edit_path('horse', 'ros'))
    print(min_edit_path_2('horse', 'ros'))

