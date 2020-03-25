import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.matching as mtc
from divDeux import abToNodes
from transfBiparti import transfBiparti_Graph
from couplageMax import couplageMax

#commentaire
#G : graph orienté acyclique
#CM : couplage max du graph biparti de G --> list de edges
#retourne list des edges de partition
def antichaine(G, CM): 
    listEdges=[]
    for e in CM:
        a, b = e
        x, y = abToNodes(a, b)
        listEdges.append((int(x), int(y)))
    return listEdges

#list des max antichaines d'un graph orienté acyclique
def partition(A):
    L = A
    for a in A :
        x, y = a
        for e in L :
            w, z = e
            if (y == w):
                L.remove(a)
                L.remove(e)
                L.append((x,z))
            if (x == z):
                L.remove(a)
                L.remove(e)
                L.append((w,y))
    return L
                

if __name__ == "__main__":
    graph = nx.DiGraph()
    elist = [(1, 2), (2, 3), (1, 4), (4, 3), (4, 5), (5, 6), (4, 7), (7, 6)]
    graph.add_edges_from(elist)

    couplage = couplageMax(transfBiparti_Graph(graph))
    anti = antichaine(graph, couplage)

    print("couplage max CM : ", couplage)
    print("max antichaine : ", anti)
    print("partition P : ", partition(anti))