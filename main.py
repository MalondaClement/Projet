import networkx as nx
from pathwidth import *
from width import *
from graphGen import *
from exGraph import *

def main(G, dico, fichier):
    nodes = nx.nodes(G)
    edges = G.edges.data('weight', default=1) #nx.edges(G)

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
    for i in range(5,25):
        for j in range(15):
            G, dict = newGraph(i, i*3)
            main(G, dict, fichier)

    fichier.close
