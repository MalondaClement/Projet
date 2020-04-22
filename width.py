import networkx as nx
import matplotlib.pyplot as plt
from graphGen import *
from partition import *
from couplageMax import *
from exGraph import *

def width(G):
    couplage = couplageMax(transfBiparti(G))
    print ("couplage : ", couplage)
    part = partition(couplage)
    print("partition P :", part)
    return len(part)

if __name__ == "__main__":
    print ("Affichage d'un graphe généré aléatoirement")
    graph, dico = graph3()
    printGraph(graph)
    print(dico)
    print("edges de graph", nx.edges(graph))

    drawGraph(graph)
    print(width(graph))