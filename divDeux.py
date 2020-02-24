import matplotlib.pyplot as plt
import networkx as nx 

def divDeux(G):
    A = []
    B = []
    for n in nx.nodes(G):
        A.append(str(n) + 'a')
        B.append(str(n) + 'b')
    return A, B

graph = nx.Graph()
elist = [(1, 2), (2, 3), (1, 4), (1, 5), (4, 2), (2, 5)]
graph.add_edges_from(elist)

listA, listB = divDeux(graph)

print ("liste A", listA)
print ("liste B", listB)

graphBi = nx.Graph()
graphBi.add_nodes_from(listA + listB)

nx.draw(graphBi, with_labels = True)
plt.draw()
plt.show()