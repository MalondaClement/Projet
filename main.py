import networkx as nx
from pathwidth import *
from width import *
from graphGen import *
from exGraph import *

fichier = open("data.txt", "a")

#G,dict = newGraph(param)
G, dico = graph1()
pathwidth = pw(2, G, dico)
w = width(G)
nodes = nx.nodes(G)
edges = nx.edges(G)
fichier.write("\n graphe : sommets = { ")

for n in nodes : 
    fichier.write(str(n))
    fichier.write(" ")

fichier.write("} \n aretes = { ")

for e in edges :
    fichier.write(str(e))

fichier.write(" } \n resultat : pathwidth = ")
fichier.write(str(pathwidth))
fichier.write(" et width = ")
fichier.write(str(w))
print("Fait")

G, dico = graph2()
pathwidth = pw(5, G, dico)
w = width(G)
nodes = nx.nodes(G)
edges = nx.edges(G)
fichier.write("\n graphe : sommets = { ")

for n in nodes : 
    fichier.write(str(n))
    fichier.write(" ")

fichier.write("} \n aretes = { ")

for e in edges :
    fichier.write(str(e))

fichier.write(" } \n resultat : pathwidth = ")
fichier.write(str(pathwidth))
fichier.write(" et width = ")
fichier.write(str(w))
print("Fait")

G, dico = graph3()
pathwidth = pw(3, G, dico)
w = width(G)
nodes = nx.nodes(G)
edges = nx.edges(G)
fichier.write("\n graphe : sommets = { ")

for n in nodes : 
    fichier.write(str(n))
    fichier.write(" ")

fichier.write("} \n aretes = { ")

for e in edges :
    fichier.write(str(e))

fichier.write(" } \n resultat : pathwidth = ")
fichier.write(str(pathwidth))
fichier.write(" et width = ")
fichier.write(str(w))
print("Fait")

fichier.close