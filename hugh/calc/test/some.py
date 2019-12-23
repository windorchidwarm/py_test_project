#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/18 9:34 
# @Author : Aries 
# @Site :  
# @File : some.py 
# @Software: PyCharm


class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key


EPSILON = 0.1 ** 14


def calc_sqrt_2():
    low = 1.4
    high = 1.5
    mid = (low + high) / 2
    while high - low > EPSILON:
        if mid * mid > 2:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return mid


def newton(x):
    if abs(x ** 2 - 2) > EPSILON:
        return newton(x - (x ** 2 - 2)/(2 * x))
    else:
        return x


def get_k_tree(tree, k):
    return get_k_tree_help(tree, k)


def get_k_tree_help(tree, k):
    if tree is None:
        return False, 0

    left, node_left_len = get_k_tree_help(tree.get_left_child(), k)

    if left:
        return left, node_left_len

    if k - node_left_len == 1:
        return True, tree.get_root_value()

    right, node_right_len = get_k_tree_help(tree.get_right_child(), k - node_left_len - 1)

    if right:
        return right, node_right_len

    return False, node_left_len + 1 + node_right_len


if __name__ == '__main__':
    print('---------------')
    print('sqrt 2 is %s' % str(calc_sqrt_2()))
    print('sqrt 2 is %s' % str(newton(1.415)))
    print('sqrt 2 is %s' % str(newton(1.414)))
    print(0.1 * 3)
    print(3/10)