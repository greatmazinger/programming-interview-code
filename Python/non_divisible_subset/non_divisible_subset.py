import fileinput
from math import sqrt

def construct_graph( k, numbers ):
    g = {}
    for item in numbers:
        g[item] = set()
    nodes = g.keys()
    while len(nodes) > 0:
        v = nodes.pop()
        for tgt in nodes:
            if (v + tgt) % k != 0:
                g[v].add(tgt)
                g[tgt].add(v)
    return g

max_cliques = []
# See https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm
def BronKerbosch( R, P, X, g ):
    global max_cliques
    if len(P) == 0 and len(X) == 0:
        max_cliques.append(R)
        return
    new_P = set(P)
    for node in new_P:
        BronKerbosch( R | set([node]), P & set(g[node]), X & set(g[node]), g )
        P.remove(node)
        X.add(node)


# TODO: This can probably be optimized.
def choose_pivot( P, X, g ):
    nodes = list(P | X)
    pivot = nodes[0]
    nodes.remove(pivot)
    pivot_deg = len(g[pivot])
    for tgt in nodes:
        if len(g[tgt]) > pivot_deg:
            pivot = tgt
            pivot_deg = len(g[tgt])
    return pivot

def BronKerbosch_with_pivot( R, P, X, g ):
    global max_cliques
    if len(P) == 0 and len(X) == 0:
        max_cliques.append(R)
        return
    new_P = set(P)
    pivot = choose_pivot( P, X, g )
    for node in new_P - set(g[pivot]):
        BronKerbosch_with_pivot( R | set([node]), P & set(g[node]), X & set(g[node]), g )
        P.remove(node)
        X.add(node)

def nonDivisibleSubset( k, numbers ):
    print "--------------------------------------------------------------------------------"
    g = construct_graph( k, numbers )
    print "g:", str(g)
    # Have the graph, now find the largest clique
    nodes = g.keys()
    # Sort according to largest degree
    sorted_nodes = sorted( nodes, 
                           key = lambda x: len(g[x]),
                           reverse = True )
    BronKerbosch_with_pivot( set(), set(sorted_nodes), set(), g )
    print "--------------------------------------------------------------------------------"
    print str(max_cliques)
    assert(len(max_cliques) > 0)
    curmax = max_cliques[0]
    for clique in max_cliques[1:]:
        if len(clique) > len(curmax):
            curmax = clique
    print "Max clique:", str(curmax)
    return len(curmax)

if __name__ == "__main__":
    filein = fileinput.input()
    num_k = filein.next().rstrip().split()
    n = int(num_k[0])
    k = int(num_k[1])
    numbers = map(int, filein.next().rstrip().split())
    print n, k
    print str(numbers)
    print nonDivisibleSubset(k, numbers)

