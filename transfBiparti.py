import matplotlib.pyplot as plt
import networkx as nx   
from divDeux import divDeux
import networkx.algorithms.matching as mtc

#commentaire
#retourne la liste des arêtes du graphe biparti H
def transfBiparti_Edges (G):
    listEdges=[]
    A, B = divDeux(G)
    for n in nx.nodes(G):
       neighbo = G.successors(n)
       for e in neighbo :
           listEdges.append((A[n-1], B[e-1]))
    return listEdges

#retourne LE graph biparti H
def transfBiparti_Graph(G):
    listEdges=[]
    A, B = divDeux(G)
    for n in nx.nodes(G):
       neighbo = G.successors(n)
       for e in neighbo :
           listEdges.append((A[n-1], B[e-1]))
    H = nx.Graph()
    H.add_edges_from(listEdges)
    return H

if __name__ == "__main__":
    graph = nx.DiGraph()
    elist = [(1, 2), (2, 3), (1, 4), (4, 3), (4, 5), (5, 6), (4, 7), (7, 6)]
    graph.add_edges_from(elist)

    H_edges = transfBiparti(graph)
    print ("liste edges de H", H_edges)

    H = nx.Graph()
    H.add_edges_from(H_edges)
    nx.draw(H, with_labels = True)
    plt.draw()
    plt.show()