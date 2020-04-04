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

def dfs_iter( G, # graph
              discovered, # list of discovered flag, 1 to 1 with nodes in G
              node # start at this node
            ):
    stack = [ node ]
    while len(stack) > 0:
        src = stack.pop()
        if not discovered[src]:
            discovered[src] = 1
            print src,
            for tgt in nx.all_neighbors(G, src):
                stack.append(tgt)

def dfs_iter2( G, # graph
               discovered, # list of discovered flag, 1 to 1 with nodes in G
               node # start at this node
             ):
    # Slightly more complicated that dfs_iter, but will produce
    # the same order as dfs_rec.
    stack = [ node ]
    while len(stack) > 0:
        src = stack.pop()
        if not discovered[src]:
            discovered[src] = 1
            print src,
            neighbors = reversed(list(nx.all_neighbors(G, src)))
            # To get the same order as recursive, we reverse the
            # order in which we insert the nodes.
            for tgt in neighbors:
                stack.append(tgt)

G = nx.moebius_kantor_graph()
print "Nodes:", G.nodes()
print "Edges:", G.edges()

discovered = [ 0 for x in xrange(G.number_of_nodes()) ]
# discovered[i] = 1 if ith node is discovered
print "Discovered array before:", discovered
root = randrange(0, G.number_of_nodes())
print "Randomly select the root node:", root

print "======================================================================"

print "DFS (recursive) from %d" % root
dfs_rec( G, discovered, root )
print

print "======================================================================"

print "DFS (iterative) from %d" % root
discovered = [ 0 for x in xrange(G.number_of_nodes()) ]
dfs_iter( G, discovered, root )
print

print "======================================================================"

print "DFS (iterative version 2) from %d" % root
discovered = [ 0 for x in xrange(G.number_of_nodes()) ]
dfs_iter2( G, discovered, root )
print

print "======================================================================"
