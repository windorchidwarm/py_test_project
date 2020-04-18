#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : aera.py
# Author: chen
# Date  : 2020-04-18

from typing import List

def maxArea(height: List[int]) -> int:
    first = 0
    last = len(height) - 1
    area = 0
    while first < last:
        area = max(area, min(height[first], height[last]) * (last - first))
        if height[first] < height[last]:
            first += 1
        else:
            last -= 1
    return area