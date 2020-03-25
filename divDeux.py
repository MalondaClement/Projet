import matplotlib.pyplot as plt
import networkx as nx 

#division en 2 listes symétriques de noeuds à partir des noeuds du graphe G
def divDeux(G):
    A = []
    B = []
    for n in nx.nodes(G):
        A.append(str(n) + 'a')
        B.append(str(n) + 'b')
    return A, B


def abToNodes(x, y):
    return (x.replace('a', ''), y.replace('b', ''))

if __name__ == "__main__":
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