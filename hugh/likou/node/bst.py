#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : bst.py
# Author: chen
# Date  : 2020-05-05

from hugh.likou.node.tree_node import TreeNode
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

if __name__ == '__main__':
    isValidBST(None)