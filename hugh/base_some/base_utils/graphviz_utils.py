#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : graphviz_utils.py
# Author: hugh
# Date  : 2020/6/29

from sklearn import tree
import os
import graphviz


def export_graph_tree(clf):
    dot_data = tree.export_graphviz(clf, out_file=None)
    os.environ["PATH"] += os.pathsep + r'E:\software\graphviz\bin'
    graph = graphviz.Source(dot_data)
    graph.view()