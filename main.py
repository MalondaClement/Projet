import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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
    return pw, w

if __name__ == "__main__":

    fichier = open("data.txt", "a")
    size = []
    res_moy_pw = []
    res_moy_w = []

    for i in range(5,100):
        fichier.write("\n")
        tmp_pw = []
        tmp_w = []
        for j in range(15):
            G, dict = newGraph(i, i*3)
            pw, w = main(G, dict, fichier)
            tmp_pw.append(pw)
            tmp_w.append(w)

        size.append(i)
        res_moy_pw.append(np.mean(tmp_pw))
        res_moy_w.append(np.mean(tmp_w))

    plt.plot(size, res_moy_pw)
    plt.plot(size, res_moy_w)
    plt.xlabel('Nombre de sommets dans le graphe')
    plt.legend(['pw','w'])
    plt.show()

    fichier.close
