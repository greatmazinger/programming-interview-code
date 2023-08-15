class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Check for when one or both are Empty
    if (p and not q) or (not p and q):
        return False
    elif not p and not q:
        return True
    # Everything else
    if p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return False

def construct_tree(tree_as_list: List) -> TreeNode:
    return Treenode()

def test1():
    assert False

if __name__ == "__main__":
    test1()
