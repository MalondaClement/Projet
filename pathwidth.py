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

# def getC(G):
#     """
#     """
#     return nx.dijkstra_path_length(G,'init','final')

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
    print(G.edges.data('weight', default=1))
    print(rG.edges.data('weight', default=1))
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
    c = r[m]+1
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
    for i in range(1, G.number_of_nodes()+1):
        res[i] = (r[i],d[i])
    return res

if __name__ == "__main__":
    G, w = graph1()
    print(inter(G,w))
    print("\n")
    G, w = graph2()
    print(inter(G,w))
    print("\n")
    G, w = graph3()
    print(inter(G,w))
