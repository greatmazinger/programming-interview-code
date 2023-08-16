class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

MAXVAL = pow(10, 5)

def getMaximum(node: TreeNode) -> int:
    mymax = node.val
    cur = node
    while cur.right:
        mymax = cur.right.val
        cur = cur.right
    return mymax


def getMinimum(node: TreeNode) -> int:
    mymin = node.val
    cur = node
    while cur.left:
        mymin = cur.left.val
        cur = cur.left
    return mymin

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    if root is None:
        return MAXVAL
    left = abs(root.val - getMaximum(root.left)) if root.left else MAXVAL
    right = abs(root.val - getMinimum(root.right)) if root.right else MAXVAL
    candlist = [left, right]
    if root.left:
        candlist.append(getMinimumDifference(root.left))
    if root.right:
        candlist.append(getMinimumDifference(root.right))
    return min(candlist)
