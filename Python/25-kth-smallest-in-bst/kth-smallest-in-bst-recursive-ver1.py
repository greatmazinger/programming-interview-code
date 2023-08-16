# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    result = countForKthSmallest(root, k, -1) # -1 as a sentinel value to indicate we're
    # looking for the smallest to start counting
    return result[2]

def countForKthSmallest(self, root: TreeNode, k: int, count: int) -> Tuple[int, bool, int]:
    # root can't be None.
    if count == -1:
        # Still looking:
        if root.left is None:
            # Found it
            newcount = 1
            found = (newcount == k)
            if found or root.right is None:
                return (newcount, found, root.val)
            else:
                # Go right
                return self.countForKthSmallest(root.right, k, newcount)
        else:
            # Still looking...
            result = self.countForKthSmallest(root.left, k, count)
            found = result[1]
            if found:
                return result
            count = result[0] + 1 # +1 for root
            if count == k or root.right is None:
                return (count, count == k, root.val)
            else:
                # Go right
                return self.countForKthSmallest(root.right, k, count)
    else:
        # Still looking...
        if root.left:
            result = self.countForKthSmallest(root.left, k, count)
            found = result[1]
            if found:
                return result
            count = result[0]
        count += 1 # +1 for root
        if count == k or root.right is None:
            return (count, count == k, root.val)
        else:
            # Go right
            return self.countForKthSmallest(root.right, k, count)

def test1():
    assert False


if __name__ == "__main__":
    test1()
