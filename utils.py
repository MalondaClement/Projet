import matplotlib.pyplot as plt
import networkx as nx 

def nodesBiparti(G):
    """creation des 2 liste A et B avec les k sommets de G
        pour construction du graph bibparti futur
    """
    A = []
    B = []
    for n in nx.nodes(G):
        A.append(str(n) + 'a')
        B.append(str(n) + 'b')
    return A, B

def abConversion(listNodes):
    """ list(nodes) --> list(nodes)
        list(dict.fromkeys(...)) élimine les doublons
    """
    nodes = [n.replace('a', '') if n[-1] == 'a' else n.replace('b', '') for n in listNodes]
    return list(dict.fromkeys(nodes))

def edgesToNodes(L):
    """ list(edges) --> list(nodes)
        créer la liste de sommets qui apparaissent dans la liste des arcs L
    """
    res=[]
    for e in L :
        x, y = e
        if x not in res :
            res.append(x)
        if y not in res :
            res.append(y)
    return abConversion(res)

def edgesRightSens(L):
    res=[]
    for e in L:
        x, y = e
        if(x[-1]=='b'):
            res.append((y, x))
        else :
            res.append((x, y))
    return res

def listEdgesBiparti(H):
    """return the edges list from a graph biparti with the good direction of the axes
        for all (x,y) : x is from side A et y from side B
    """
    return edgesRightSens(nx.edges(H))

def edgeABtoedge(e):
    """ edge --> edge
    """
    x, y = e
    if(x[-1] == 'a' and y[-1] == 'b'):
        return (x.replace('a', ''), y.replace('b', ''))
    
    return (x.replace('b', ''), y.replace('a', ''))