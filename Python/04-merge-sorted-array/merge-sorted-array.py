from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Move first m elements in nums1 to the end
    for i in range(m - 1, -1, -1):
        nums1[i + n] = nums1[i]
    # Now do the merge:
    i = n
    j = 0
    cur = 0
    while (i < m + n) and (j < n):
        if nums1[i] <= nums2[j]:
            nums1[cur] = nums1[i]
            i = i + 1
            cur = cur + 1
        else:
            nums1[cur] = nums2[j]
            j = j + 1
            cur = cur + 1
    if cur < m + n:
        if (i < m + n):
            while (i < m + n):
                nums1[cur] = nums1[i]
                i = i + 1
                cur = cur + 1
        elif j < n:
            while (j < n):
                nums1[cur] = nums2[j]
                j = j + 1
                cur = cur + 1

def test1():
    print("Running TEST 1:")
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 4, 5]

    expected = [1, 2, 2, 3, 4, 5]
    merge(nums1, 3, nums2, 3)
    for i in range(len(expected)):
        assert nums1[i] == expected[i]
    print(" -- TEST 1 SUCCESS.")

if __name__ == "__main__":
    test1()
