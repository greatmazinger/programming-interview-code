import networkx as nx
from random import randrange

G = nx.moebius_kantor_graph()
print "Nodes:", G.nodes()
print "Edges:", G.edges()

discovered = [ 0 for x in xrange(G.number_of_nodes()) ]
# discovered[i] = 1 if ith node is discovered
print "Discovered array before:", discovered
root = randrange(0, G.number_of_nodes())
print "Randomly select the root node:", root
