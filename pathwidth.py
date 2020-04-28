import networkx as nx
import matplotlib.pyplot as plt
from graphGen import newGraph, drawGraph, printGraph
from exGraph import graph1, graph2, graph3


def addInitAndFinalState(G, dict):
    """This function adds a commun initial (and final) state to the graph for each state without predecessor (or successor)
        :param arg1: graph G
        :param arg2: dictionary with the time of execution of each task
        :type arg1: networkx DiGraph
        :type arg2: dictionary
        :return: graph newG with init and final node
        :rtype: networkx DiGraph
    """
    newG = nx.DiGraph()
    newG.add_node('init')
    newG.add_nodes_from(G.nodes())
    newG.add_node('final')
    for e in G.edges.data('weight', default=1):
        i,j,w = e
        newG.add_edge(i,j,weight=w)
    for n in G.nodes():
        P = []
        S = []
        pTmp = G.predecessors(n)
        for i in pTmp:
            P.append(i)
        if P == []:
            newG.add_edge('init',n,weight=0)
        sTmp = G.successors(n)
        for i in sTmp:
            S.append(i)
        if S == []:
            w = dict.get(n)
            newG.add_edge(n,'final',weight=w)
    return newG

def reverseGraph(G,dict):
    """
    """
    rG = nx.DiGraph()
    rG.add_nodes_from(G.nodes())
    for e in G.edges(): #.data('weight', default=1):
        i, j, = e
        w = 0
        if i == 'init':
            w = 0
        else :
            w = dict[i]
        rG.add_edge(j,i,weight=w)
    return rG

def inter(G, dict):
    nodes = G.nodes()
    G1 = addInitAndFinalState(G, dict)
    G2 = reverseGraph(G1,dict)
    res = {}
    topo = nx.topological_sort(G)
    r = {}
    for e in topo:
        tmp = 0
        for p in G1.predecessors(e):
            if p == 'init':
                tmp = 0
            else:
                tmp = max(tmp, r[p] + dict[e])
        r[e] = tmp
    m = max(r)
    c = r[m]+dict[m]
    topo = nx.topological_sort(G2)
    d = {}
    for e in topo:
        tmp = c + 1
        if e == 'init' or e == 'final':
            continue
        for p in G2.predecessors(e):
            if p == 'final':
                tmp = c + 1
            else:
                tmp = min(tmp, d[p] - dict[e])
        d[e] = tmp
    for i in G.nodes():
        res[i] = (r[i],d[i])
    return res, m

def pw(G, dict):
    dict_inter, m = inter(G, dict)
    tab = set()
    res = {}
    for i in dict_inter:
        tab.add(dict_inter[i][0])
        tab.add(dict_inter[i][1])
    for i in tab:
        res[i] = 0
        for e in dict_inter:
            if i >= dict_inter[e][0] and i <= dict_inter[e][1]:
                res[i] += 1
    return min(max(res.values()), m)



if __name__ == "__main__":
    G, w = graph1()
    print(pw(G, w))
    print(inter(G,w))
    print("\n")
    G, w = graph2()
    print(pw(G, w))
    print(inter(G,w))
    print("\n")
    G, w = graph3()
    print(pw(G, w))
    print(inter(G,w))
