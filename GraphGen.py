import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from random import randint

def newGraph(nodes=10, edges=24, weight=True):
    """ This function use an undirected graph from networkx to creat a directed graph without circuit.
        :param arg1: Numbers of nodes in the graph
        :param arg2: Numbers of edges in the graph
        :param arg3: Add random weight on edges if True
        :type arg1: int
        :type arg2: int
        :type arg3: boolean
        :return: Return a directed graph without circuit
        :rtype: DiGraph
    """
    tmp = nx.gnm_random_graph(nodes, edges)
    G = nx.DiGraph()
    G.add_nodes_from(tmp.nodes())
    if weight:
        for i in tmp.edges():
            G.add_edge(*i,weight=randint(1,6))
    else:
        for i in tmp.edges():
            G.add_edge(*i)
    return G

def biPartiteGraph(G):
    """ This function use a directed graph to generate a bipartite braph
        :param arg1: Directed Graph
        :type arg1: DiGraph
        :return: Return a directed graph without circuit
        :rtype: Graph
    """
    B = nx.Graph()
    nodesList1 = []
    nodesList2 = []
    for i in range(len(G.nodes())):
        nodesList1.append(i+0.0)
        nodesList2.append(i+0.1)
    B.add_nodes_from(nodesList1, bipartite=0)
    B.add_nodes_from(nodesList2, bipartite=1)
    for i in G.nodes():
        for j in G.successors(i):
            B.add_edge(nodesList1[i],nodesList2[j])
    return B

def findIndependantSet(B):
    """This function use a bipartite graph to foud independent set
    """
    matching = bipartite.maximum_matching(B)
    print(matching)
    # vertex_cover = bipartite.to_vertex_cover(B, matching)
    # independent_set = set(B) - vertex_cover
    # print(list(independent_set))

def printGraph(G,isBipartite=False):
    """This function is used to print a graph's informatin
    """
    print("Liste des sommets : " + str(G.nodes()))
    print("Liste des arcs : " + str(G.edges()))
    print("Liste des arcs avec poids: " + str(G.edges.data('weight', default=1)))
    for i in G.nodes():
        print("Les succeseurs de " + str(i) + " sont " + str(G.successors(i)))
    if not isBipartite:
        print("Plus long chemin : " + str(nx.dag_longest_path(G)) + ", longueur du plus long chemin : " + str(nx.dag_longest_path_length(G)))
    print("\n\n")

def drawGraph(G):
    """This function to creat a graphic representation of a graph
    """
    nx.draw(G, with_labels=1)
    plt.draw()
    plt.show()

if __name__ == "__main__":
    print("Generation d'un graphe aleatoire")

    G = newGraph()
    printGraph(G)

    B = biPartiteGraph(G)
    # findIndependantSet(B)

    drawGraph(G)
    drawGraph(B)