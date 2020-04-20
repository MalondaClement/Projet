import networkx as nx

def graph1():
    G = nx.DiGraph()
    G.add_nodes_from((1,2,3,4,5,6,7))
    G.add_edges_from(((1,2),(2,3),(1,4),(4,5),(4,6),(6,7),(5,7)))
    dict = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1}
    return G, dict

def graph2():
    G = nx.DiGraph()
    G.add_nodes_from((1,2,3,4,5,6,7))
    G.add_edges_from(((1,2),(2,3),(4,5),(6,7)))
    dict = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1}
    return G, dict

def graph3():
    G = nx.DiGraph()
    G.add_nodes_from((1,2,3,4,5,6))
    G.add_edges_from(((1,4),(1,5),(2,6),(3,6)))
    dict = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1}
    return G, dict
