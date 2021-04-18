# Given two sorted arrays (A and B), find the median of the two when merged.
# 

# Test cases:
#
#   Case 1:
#       Regular test case where each array contributes to the left and right interval
#       Example -
#           A = [ 1, 3, 5, 9, 11, 12, 13 ]
#           B = [ 2, 4, 6, 7, 8 ]
#
#   Case 2:
#       One list is empty.   
#           A = [ 1, 2, 3, 4, 5, 6, 7 ]
#           B = [ ]
#
#   Case 3:
#       One list with one element. Worth mentioning just to make sure this is handled properly in the general Case 1.   
#           A = [ 1, 2, 3, 4, 5, 7, 8, 9 ]
#           B = [ 6 ]

#
#   Solution outline:
#       The general idea is to partition all the elements in A and B into left and right sets that are equal
#       where the partitioning element is by definition the median.

def run_test_case_1(solver):
    A = [ 1, 3, 5, 9, 11, 12, 13 ]
    B = [ 2, 4, 6, 7, 8 ]
    expected = 7

    assert(callable(solver))
    result = solver(A, B)
    try:
        assert(result == expected)
        print("Test case 1 passed.")
    except:
        print("Test case 1 (Regular input) failed. Expected = %d | Actual = %d" % (result, expected)

def merge_ver01():
    pass

if __name__ == "__main__":
    pass
