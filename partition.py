import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.matching as mtc
from utils import *
from transfBiparti import *
from couplageMax import *

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

if __name__ == "__main__":
    graph = nx.DiGraph()
    elist = [(1, 2), (2, 3), (1, 4), (4, 3), (4, 5), (5, 6), (4, 7), (7, 6)]
    graph.add_edges_from(elist)

    couplage = couplageMax(transfBiparti_Graph(graph))
    anti = antichaine(graph, couplage)
    print("arêtes du graph G : ", elist)
    print("couplage max CM : ", couplage)
    print("max antichaine : ", anti)
    print("partition P : ", partition(anti))