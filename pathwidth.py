import networkx as nx
import matplotlib.pyplot as plt
from grapheGen import newGraph, drawGraph, printGraph

def addInitAndFinalState(G):
    newG = nx.DiGraph()
    newG.add_nodes_from(G.nodes())
    newG.add_node('init')
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
            newG.add_edge(n,'final',weight=4)
    print(newG.edges.data('weight', default=1))
    return newG

def getC(G):
    # changer 0 en init et 9 en final
    return nx.dijkstra_path_length(G,'init','final')

if __name__ == "__main__":
    G = newGraph(weight=True)
    GWithIF = addInitAndFinalState(G)
    c = getC(GWithIF)
    print(c)
