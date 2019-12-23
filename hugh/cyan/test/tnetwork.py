#encoding:utf-8

import networkx as nx

nodes = {"1": {"nid":"1", "eid":"2", "type":"11", "isEnd":"0"},
         "2": {"type":"11", "isEnd":"0"},
         "3": {"type":"21", "isEnd":"1"}}

edges = [{"start_node_id":"1", "end_node_id":"3"},
         {"start_node_id":"2", "end_node_id":"3"}]

dg = nx.DiGraph()

for id,prop in nodes.items():
    dg.add_node(id, **prop)

nodeRelation = {}
for edge in edges:
    start = edge.get("start_node_id")
    end = edge.get("end_node_id")
    dg.add_edge(start, end)
    if nodeRelation.get(end) is None:
        nodeRelation[end] = set()
    nodeRelation[end].add(start)

#print(dg)
print(dg.edges)
print(nodeRelation)
print(dg.in_degree)
print(dg.in_edges)

#
def get0InDegreeNodes(dg):
    ret = []
    nodeDegrees = dg.in_degree
    for n in nodeDegrees:
        if n[1] == 0:
            ret.append(n[0])
    dg.remove_nodes_from(ret)
    return ret

nodes = get0InDegreeNodes(dg)
print(nodes)
print(dg.in_degree)
nodes = get0InDegreeNodes(dg)
print(nodes)
print(dg.in_degree)