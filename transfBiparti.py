import matplotlib.pyplot as plt
import networkx as nx   
from divDeux import divDeux
import networkx.algorithms.matching as mtc


def transfBiparti (G):
    listEdges=[]
    A, B = divDeux(G)
    for n in nx.nodes(G):
       neighbo = G.successors(n)
       for e in neighbo :
           listEdges.append((A[n-1], B[e-1]))
    return listEdges


graph = nx.DiGraph()
elist = [(1, 2), (2, 3), (1, 4), (1, 5), (4, 5), (2, 5)]
graph.add_edges_from(elist)
#nx.draw(graph, with_labels = True)

biparti = transfBiparti(graph)
print ("biparti", biparti)

graphBi = nx.Graph()
graphBi.add_edges_from(biparti)

print ("maximal matching", mtc.maximal_matching(graphBi))
nx.draw(graphBi, with_labels = True)
plt.draw()
plt.show()