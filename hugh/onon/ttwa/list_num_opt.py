#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/30 11:11 
# @Author : Aries 
# @Site :  
# @File : list_num_opt.py 
# @Software: PyCharm


class ListNumOpt:
    def findKSortedArrays(self, nums1, nums2, k):
        '''
        nums1 m 和 nums2 n分别是对应的有序数组和其长度，k是求的第k小的书

        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :param k:
        :return:
        '''
        def findKSortedArraysSol(nums1, m, nums2, n, k):
            if m > n:
                return findKSortedArraysSol(nums2, n, nums1, m, k)
            if m == 0:
                return nums2[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            pa = min(int(k/2), m)
            pb = k - pa
            if nums1[pa - 1] > nums2[pb - 1]:
                return findKSortedArraysSol(nums1, m, nums2[pb:], n - pb, k - pb)
            elif nums1[pa - 1] < nums2[pb - 1]:
                return findKSortedArraysSol(nums1[pa:], m - pa, nums2, n, k - pa)
            else:
                return nums1[pa - 1]

        findKSortedArraysSol(nums1, len(nums1), nums2, len(nums2), k)
