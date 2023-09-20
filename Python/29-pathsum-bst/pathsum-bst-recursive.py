from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return targetSum == root.val
    # Go left:
    if root.left is not None and hasPathSum(root.left, targetSum - root.val):
        return True
    # Go right:
    if root.right is not None and hasPathSum(root.right, targetSum - root.val):
        return True
    # Go back:
    return False

def test1():
    assert False
    # TODO:


if __name__ == "__main__":
    test1()
