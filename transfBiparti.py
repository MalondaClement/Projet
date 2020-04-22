import matplotlib.pyplot as plt
import networkx as nx   
from utils import nodesBiparti
from graphGen import *
import networkx.algorithms.matching as mtc

def transfBiparti(G):
    """graph oriente acyclique --> graph biparti H
    """
    H = nx.Graph()
    A, B = nodesBiparti(G)
    for n in nx.nodes(G):
        neighbo = G.successors(n)
        for e in neighbo :
            H.add_edge(A[n], B[e])
    return H