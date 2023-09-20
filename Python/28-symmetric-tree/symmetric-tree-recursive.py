from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if left is None and right is None:
        return True
    if (left is None and right is not None) or  (left is not None and right is None):
        return False
    if (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left):
        return True
    else:
        return False

def isSymmetric(root: Optional[TreeNode]) -> bool:
    return isMirror(root.left, root.right)

# TODO
def create_tree(tree_array):
    pass

def test1():
    pass

if __name__ == "__main__":
    test1()
