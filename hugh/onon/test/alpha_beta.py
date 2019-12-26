#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : alpha_beta.py
# Author: chen
# Date  : 2019-11-25


# //node记录当前player，depth记录搜索深度
# function mini_max(node, depth)
#    // 如果能得到确定的结果或者深度为零，使用评估函数返回局面得分
#    if node is a terminal node or depth = 0
#        return the heuristic value of node
#    // 如果轮到对手走棋，是极小节点，选择一个得分最小的走法
#    if the adversary is to play at node
#        let α := +∞
#        for each child of node
#            α := min(α, mini_max(child, depth-1))
#    // 如果轮到我们走棋，是极大节点，选择一个得分最大的走法
#    else {we are to play at node}
#        let α := -∞
#        foreach child of node
#            α := max(α, mini_max(child, depth-1))
#    return α;
#  https://blog.csdn.net/qq_31615919/article/details/79681063

class Node(object):
    def __index__(self, name):
        self.name = name
        self.value = -1
        self.p_father = ''
        self.p_children = []


MAX_INT=32767
MIN_INT=-32768
MAX=1
MIN=0


node_tree = []
del_zhi = []
del_count = 0

def get_strategy(input_file):
    read_tree(input_file)
    alpha_beta(node_tree[0].name)
    best_route = ''
    for i in range(len(node_tree[0].p_children)):
        if node_tree[0].value == node_tree[search(node_tree[0].pChildren[i])].value:
            best_route = node_tree[0].name + node_tree[0].value
            break

def alpha_beta(name):
    flag = False
    n_node = node_tree[search(name)]
    if n_node.levle == MAX:
        for j in range(len(n_node.p_children)):
            alpha_beta(n_node.p_children[j])
            if n_node.value < node_tree[search(node_tree[0].pChildren[j])].value:
                n_node.value = node_tree[search(node_tree[0].pChildren[j])].value
                if beta(name):
                    del_zhi[del_count] = name + ":"
                    for k in range(j+1, len(n_node.p_children)):
                        del_zhi[del_count] = del_zhi[del_count] + " " + n_node.p_children[j] + " β剪枝 "
                        flag = True
                    if flag:
                        del_count = del_count + 1
                    return
    else:
        for j in range(len(n_node.p_children)):
            alpha_beta(n_node.p_children[j])
            if n_node.value > node_tree[search(node_tree[0].pChildren[j])].value:
                n_node.value = node_tree[search(node_tree[0].pChildren[j])].value
                if alpha(name):
                    del_zhi.insert(del_count, name + ":")
                    # del_zhi[del_count] = name + ":"
                    for k in range(j+1, len(n_node.p_children)):
                        del_zhi[del_count] = del_zhi[del_count] + " " + n_node.p_children[j] + " α剪枝 "
                        flag = True
                    if flag:
                        del_count = del_count + 1
                    return
def alpha(name):
    n_node = node_tree[search(name)]
    if n_node.p_father is None:
        return False
    i = search(node_tree.p_father)
    while i >= 0:
        if node_tree[i].value >= n_node.value and node_tree[i].level == MAX and node_tree[i].value != MIN_INT:
            return True
        else:
            if i != 0:
                i = search(node_tree[i].p_father)
            else:
                break
    return False

def beta(name):
    n_node = node_tree[search(name)]
    if n_node.p_father is None:
        return False
    i = search(node_tree.p_father)
    while i >= 0:
        if node_tree[i].value <= n_node.value and node_tree[i].level == MIN and node_tree[i].value != MAX_INT:
            return True
        else:
            if i != 0:
                i = search(node_tree[i].p_father)
            else:
                break
    return False


def search(name):
    for j in range(len(node_tree)):
        if node_tree[j].name.equals(name):
            return j
    return -1

def read_tree(file_path):
    return ''
#         File
#         file = new
#         File(filename);
#         String
#         nodename[] = new
#         String[10];
#         try
#             {
#                 BufferedReader in = new
#             BufferedReader(new
#             FileReader(file));
#             String
#             s;
#             s = in.readLine();
#             if (s.startsWith("ROOT"))
#             {
#             nodename=s.split("\\s+");
#             }
#             NodeTree.add(new Node(nodename[1]));
#             NodeTree.get(0).leval=MAX;
#             NodeTree.get(0).value=MIN_INT;
#             NodeTree.get(0).pFather=null;
#         while (!(s= in.readLine()).equals("VALUE"))
#         {
#             nodename = s.split("\\s+");
#         for (int i=1;i < nodename.length-1;i++)
#         {
#             NodeTree.get(search(nodename[0])).pChildren.add(nodename[i]);
#         Node nNode=new Node(nodename[i]); // value为-1；
#         nNode.pFather=nodename[0];
#         if (NodeTree.get(search(nodename[0])).leval == MAX)
#         {
#         nNode.leval=MIN;
#         nNode.value=MAX_INT;
#         }
#         else
#         {
#         nNode.leval=MAX;
#         nNode.value=MIN_INT;
#         }
#         NodeTree.add(nNode);
#         }
#         }
#         String
#         nodeValue[] = new
#         String[10];
#         while (!(s= in.readLine()).equals("END"))
#         {
#             nodeValue = s.split("\\s+");
#         NodeTree.get(search(nodeValue[0])).value = Integer.parseInt(nodeValue[1]);
#         }
#         in.close();
#
# }catch(Exception
# e){
# System.out.println("Error!!");}
# }


if __name__ == '__main__':
    print('f')
