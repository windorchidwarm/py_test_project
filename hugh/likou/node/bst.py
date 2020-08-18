#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : bst.py
# Author: chen
# Date  : 2020-05-05

from hugh.likou.node.tree_node import TreeNode
from hugh.likou.node.list_node import ListNode
from typing import List
import numpy as np

def isValidBST(root: TreeNode) -> bool:
    '''
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。
    假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    :param self:
    :param root:
    :return:
    '''
    def helper(node, lower = np.float('-inf'), upper = np.float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)

def sortedListToBST(self, head: ListNode) -> TreeNode:
    '''
    给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
    给定的有序链表： [-10, -3, 0, 5, 9],

    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5
    :param self:
    :param head:
    :return:
    '''
    def getLength(head:ListNode) -> int:
        ret = 0
        while head:
            ret += 1
            head = head.next
        return ret

    def buildTree(left:int, right:int) -> TreeNode:
        if left > right: return None
        mid = (right + left + 1) // 2
        root = TreeNode()
        root.left = buildTree(left, mid - 1)
        nonlocal head
        root.val = head.val
        head = head.next
        root.right = buildTree(mid + 1, right)
        return root
    length = getLength(head)
    return buildTree(0, length - 1)

if __name__ == '__main__':
    isValidBST(None)