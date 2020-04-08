import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.matching as mtc
from transfBiparti import *
from utils import *

def couplageMax(H):
    """return la liste des arcs appartenant au couplage maximal
    """

    cMax = edgesRightSens(mtc.maximal_matching(H))
    nodes_cMax = edgesToNodes(cMax)
    nodes_H = abConversion(nx.nodes(H))
    
    for n in nodes_H:
        if(n not in nodes_cMax):
            cMax.append( (n+'a', n+'b') )

    return cMax

if __name__ == "__main__":
    graph = nx.DiGraph()
    elist = [(1, 2), (2, 3), (1, 4), (4, 3), (4, 5), (5, 6), (4, 7), (7, 6)]
    graph.add_edges_from(elist)

    print (couplageMax(transfBiparti_Graph(graph)))


