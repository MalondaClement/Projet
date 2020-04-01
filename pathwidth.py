import networkx as nx
import matplotlib.pyplot as plt
from graphGen import newGraph, drawGraph, printGraph

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

if __name__ == "__main__":
    G, w = newGraph(weight=True)
    GWithIF = addInitAndFinalState(G, w)
    print(GWithIF.edges.data('weight', default=1))
    rG = returnGraph(GWithIF)
    print(rG.edges.data('weight', default=1))
