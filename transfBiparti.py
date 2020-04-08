import matplotlib.pyplot as plt
import networkx as nx   
from utils import nodesBiparti
from graphGen import *
import networkx.algorithms.matching as mtc

def transfBiparti(G):
    """graph oriente acyclique --> graph biparti H
    """
    H = nx.Graph()
    A, B = nodesBiparti(G)
    for n in nx.nodes(G):
        neighbo = G.successors(n)
        for e in neighbo :
            H.add_edge(A[n], B[e])
    return H

if __name__ == "__main__":
    graph = nx.DiGraph()
    elist = [(1, 2), (2, 3), (1, 4), (4, 3), (4, 5), (5, 6), (4, 7), (7, 6)]
    graph.add_edges_from(elist)

    H_edges = transfBiparti_Edges(graph)
    print ("liste edges de H", H_edges)

    H = nx.Graph()
    H.add_edges_from(H_edges)
    print("edges de H", nx.edges(H))
    print("nodesd de H", nx.nodes(H))
    nx.draw(H, with_labels = True)
    plt.draw()
    plt.show()