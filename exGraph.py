import networkx as nx

def graph1():
    G = nx.DiGraph()
    G.add_nodes_from((0,1,2,3,4,5,6))
    G.add_edges_from(((0,1),(1,2),(0,3),(3,4),(3,5),(5,6),(4,6),(2,6)))
    dict = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
    return G, dict

def graph2():
    G = nx.DiGraph()
    G.add_nodes_from((0,1,2,3,4,5,6))
    G.add_edges_from(((0,1),(1,2),(3,4),(5,6)))
    dict = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
    return G, dict

def graph3():
    G = nx.DiGraph()
    G.add_nodes_from((0,1,2,3,4,5))
    G.add_edges_from(((0,3),(0,4),(1,5),(2,5)))
    dict = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
    return G, dict
