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
    for n in nx.nodes(G):
        neighbo = G.successors(n)
        for e in neighbo :
            H.add_edge(A[n], B[e])
    return H

def couplageMax(H):
    """return la liste des arcs appartenant au couplage maximal
    """

    cMax = edgesRightSens(mtc.maximal_matching(H))
    nodes_cMax = edgesToNodes(cMax)
    nodes_H = abConversion(nx.nodes(H))
    
    for n in nodes_H:
        if(n not in nodes_cMax):
            cMax.append( (n+'a', n+'b') )
    return cMax

def antichaine(CM):
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
    antiCh = antichaine(CM)

    for c in antiCh:
        x, y = c
        if(len(P)==0):
            P.append([x,y])
        
        elif(x==y):
            P.append([x])
        
        else:
            ajout = False

            for i in range(len(P)) :
                if(x in P[i]):
                    if(y not in P[i]):   
                        P[i].append(y)
                        ajout = True
                
                elif(y in P[i]):
                    if(x not in P[i]):
                        P[i].append(x)
                        ajout = True
            
            if(not ajout):
                P.append([x, y])
    return P               

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