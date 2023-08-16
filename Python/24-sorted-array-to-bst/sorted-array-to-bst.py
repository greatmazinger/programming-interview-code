class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return TreeNode(nums[0], None, None)
    mid = len(nums) // 2
    left_tree = sortedArrayToBST(nums[0:mid])
    right_tree =sortedArrayToBST(nums[mid+1:len(nums)])
    return TreeNode(nums[mid], left_tree, right_tree)

def test1():
    pass
    # TODO


if __name__ == "__main__":
    test1()
