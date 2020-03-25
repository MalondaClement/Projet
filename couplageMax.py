import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.matching as mtc
from transfBiparti import transfBiparti_Graph

def couplageMax(H):
    return mtc.maximal_matching(H)

if __name__ == "__main__":
    graph = nx.DiGraph()
    elist = [(1, 2), (2, 3), (1, 4), (4, 3), (4, 5), (5, 6), (4, 7), (7, 6)]
    graph.add_edges_from(elist)

    print (couplageMax(transfBiparti_Graph(graph)))


