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

def getC(G):
    """
    """
    return nx.dijkstra_path_length(G,'init','final')

def returnGraph(G):
    """
    """
    rG = nx.DiGraph()
    rG.add_nodes_from(G.nodes())
    for e in G.edges.data('weight', default=1):
        i, j, w = e
        rG.add_edge(j,i,weight=w)
    return rG

def inter(G, dict):
    nodes = G.nodes()
    print(nodes)
    G1 = addInitAndFinalState(G, dict)
    G2 = returnGraph(G1)
    dict = {}
    for i in nodes:
        r = nx.dijkstra_path_length(G1,'init',i)
        d = nx.dijkstra_path_length(G2,'final',i)
        dict[i] = (r,d)
    return dict

if __name__ == "__main__":
    G, w = graph2()
    print(inter(G,w))
    G, w = graph3()
    print(inter(G,w))
