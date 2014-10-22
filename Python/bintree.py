# Took the code from stackoverflow:
#    https://stackoverflow.com/questions/3058665/represent-binary-search-trees-in-python
# but fixed a bug in insert where it was inserting larger values on the left. Quite the
# opposite of convention.
#
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, othernode):
        "Insert Node `othernode` under Node `self`."
        if self.value > othernode.value:
            if self.left:
                self.left.insert(othernode)
            else:
                self.left = othernode
        else:
            if self.right:
                self.right.insert(othernode)
            else:
                self.right = othernode

    def inorderwalk(self):
        "Yield this Node and all under it in increasing-value order."
        if self.left:
            for x in self.left.inorderwalk():
                yield x
        yield self
        if self.right:
            for x in self.right.inorderwalk():
                yield x
    
    def __repr__(self):
        return str(self.value)

def create_balanced_tree( srclist = None ):
    if len(srclist) == 0:
        return None
    midpt = len(srclist) // 2
    root = Node(srclist[midpt])
    if len(srclist) == 1:
        return root
    else:
        # print "LEFT", srclist[:midpt]
        left = create_balanced_tree( srclist[:midpt] )
        if left != None:
            root.insert( left )
        # print "RIGHT", srclist[midpt+1:]
        right = create_balanced_tree( srclist[midpt + 1:] )
        if right != None:
            root.insert( right )
    return root

if __name__ == "__main__":
    print "Binary tree test:"
    mylist = [1, 4, 5, 8, 14, 24, 36, 41, 43, 44, 45, 52, 64, 68, 75, 77, 81, 90, 91, 95, 99]
    print "Original list:", mylist

    root = create_balanced_tree( mylist )
    print "Root:", root
    print "Inorder traversal:"
    for x in root.inorderwalk():
        print x,
    print
