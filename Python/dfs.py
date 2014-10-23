import networkx as nx
from random import randrange

def dfs_rec( G, # graph
             discovered, # list of discovered flag, 1 to 1 with nodes in G
             node # start at this node
             ):
    discovered[node] = 1
    print node,
    for tgt in nx.all_neighbors(G, node):
        if not discovered[tgt]:
            dfs_rec( G, discovered, tgt )

G = nx.moebius_kantor_graph()
print "Nodes:", G.nodes()
print "Edges:", G.edges()

discovered = [ 0 for x in xrange(G.number_of_nodes()) ]
# discovered[i] = 1 if ith node is discovered
print "Discovered array before:", discovered
root = randrange(0, G.number_of_nodes())
print "Randomly select the root node:", root

print "DFS from %d" % root
dfs_rec( G, discovered, root )
print
