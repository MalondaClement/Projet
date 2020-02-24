import matplotlib.pyplot as plt
import networkx as nx 
from networkx.algorithms import bipartite

B = nx.Graph()
B.add_nodes_from([1, 2, 3, 4], bipartite=0)
B.add_nodes_from(['a', 'b', 'c'], bipartite = 1)

B.add_edges_from([(1, 'a'), (1, 'b'), (2, 'b'), (2, 'c'), (3, 'c'), (4, 'a'), (1, 'd')])

bottom_nodes, top_nodes = bipartite.sets(B)

print ("bottom_nodes", bottom_nodes)
print ("top_nodes",top_nodes)

biparti = bipartite.generators.complete_bipartite_graph(bottom_nodes, top_nodes, create_using=None)
nx.draw(B, with_labels = True)
plt.draw()
plt.show()