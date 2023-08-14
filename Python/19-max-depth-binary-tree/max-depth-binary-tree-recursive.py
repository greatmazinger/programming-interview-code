from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    elif root.left and root.right:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    elif root.left is None and root.right is None:
        return 1
    elif root.left:
        return 1 + self.maxDepth(root.left)
    elif root.right:
        return 1 + self.maxDepth(root.right)
    assert False

def test1():
    # TODO
    print("TODO: Implement test1. Needs a create a tree from an array spec.")
    assert False

if __name__ == "__main__":
    test1()
