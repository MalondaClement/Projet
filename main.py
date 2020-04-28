import networkx as nx
from pathwidth import *
from width import *
from graphGen import *
from exGraph import *

def main(G, dico, fichier):
    nodes = nx.nodes(G)
    edges = nx.edges(G)

    pw = pathwidth(G, dico)
    w = width(G)

    fichier.write("\n graphe : sommets = { ")

    for n in nodes : 
        fichier.write(str(n))
        fichier.write(" ")

    fichier.write("} \n aretes = { ")

    for e in edges :
        fichier.write(str(e))

    fichier.write(" } \n resultat : pathwidth = ")
    fichier.write(str(pw))
    fichier.write(" et width = ")
    fichier.write(str(w))
    print("Fait")

if __name__ == "__main__":
    
    fichier = open("data.txt", "a")

    #G,dict = newGraph(param)
    G1, dico1 = graph1()
    main(G1, dico1, fichier)

    G2, dico2 = graph2()
    main(G2, dico2, fichier)

    G3, dico3 = graph3()
    main(G3, dico3, fichier)

    fichier.close