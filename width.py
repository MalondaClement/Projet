import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.matching as mtc
from graphGen import *
from utils import *
from exGraph import *

def transfBiparti(G):
    """graph oriente acyclique --> graph biparti H
    """
    H = nx.Graph()
    A, B = nodesBiparti(G)
    for e in nx.edges(G):
        x, y = e
        H.add_edge(A[x], B[y])
    return H

def couplageMax(H):
    """return la liste des arcs appartenant au couplage maximal
    """

    cMax = (list)(mtc.maximal_matching(H))
    print("cMax :", cMax)
    nodes_cMax = abConversion(edgesToNodes(cMax))
    nodes_H = abConversion(nx.nodes(H))
    
    for n in nodes_H:
        if(n not in nodes_cMax):
            cMax.append( (n+'a', n+'b') )
    return cMax

def conversion(CM):
    """list du couplage maximale avec les sommets du graph biparti (a/b)
        return list du couplage maximale sans les suffixes 'a'/'b'
    """ 
    listEdges=[]
    for e in CM:
        x, y = edgeABtoedge(e)
        listEdges.append((int(x), int(y)))
    return listEdges

def partition(CM):
    """couplagemax d'un graphe biparti --> partition du graphe orienté acyclique correspond
        conversion du couplemage maximale du graph biparti 
        avec sommets uniques du graph orienté acyclique
    """
    P = []
    couplage = conversion(CM)

    for c in couplage:
        x, y = c
        if(len(P)==0):
            P.append([x,y])
        
        elif(x==y):
            P.append([x])
        
        else:
            ajout = False

            for k in range(len(P)) :
                if(x in P[k]):
                    if(y not in P[k]): 
                        P[k].append(y)
                        ajout = True
                
                elif(y in P[k]):
                    if(x not in P[k]):
                        P[k].append(x)
                        ajout = True
            
            if(not ajout):
                P.append([x, y])

    P = fusionPart(P)
    return P               

def width(G):
    couplage = couplageMax(transfBiparti(G))
    print ("couplage : ", couplage)
    part = partition(couplage)
    print("partition P :", part)
    return len(part)

if __name__ == "__main__":
    print ("Affichage d'un graphe généré aléatoirement")
    graph, dico = graph1()
    printGraph(graph)
    print(dico)
    print("edges de graph", nx.edges(graph))

    drawGraph(graph)
    print(width(graph))