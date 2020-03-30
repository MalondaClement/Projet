import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from random import randint

def edgesWeight(n):
    """This fuction create a dictionary with run time for each task
        :param arg1: Number of task
        :type arg1: int
        :return: Return a dictionary
        :rtype: dictionary
    """
    dict = {}
    for i in range(n):
        dict[i] = randint(1,6)
    return dict

def newGraph(nodes=8, edges=12, weight=True):
    """ This function use an undirected graph from networkx to create a directed graph without circuit.
        :param arg1: Number of nodes in the graph
        :param arg2: Number of edges in the graph
        :param arg3: Add random weight on edges if True
        :type arg1: int
        :type arg2: int
        :type arg3: boolean
        :return: Return a directed graph without circuit, and a dictionary
        :rtype: DiGraph,dictionary
    """
    tmp = nx.gnm_random_graph(nodes, edges)
    G = nx.DiGraph()
    G.add_nodes_from(tmp.nodes())
    dict = edgesWeight(nodes)
    for e in tmp.edges():
        i, j = e
        if weight:
            w = dict.get(i)
            G.add_edge(i,j,weight=w)
        else:
            dict[i] = 1
            G.add_edge(i,j,weight=1)
    return G, dict

def printGraph(G,isBipartite=False):
    """This function is used to print a graph's information
    """
    print("Liste des sommets : " + str(G.nodes()))
    print("Liste des arcs avec poids: " + str(G.edges.data('weight', default=1)))

def drawGraph(G):
    """This function to create a graphic representation of a graph
    """
    nx.draw(G, with_labels=1)
    plt.draw()
    plt.show()

if __name__ == "__main__":
    print("Test générateur de graphe")
    G, dict = newGraph()
    printGraph(G)
    print(dict)
