# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#  -> Integers in each row are sorted in ascending from left to right.
#  -> Integers in each column are sorted in ascending from top to bottom.

# main idea:
# Relax problem to a square matrix and consider the subproblem of
# finding an element in a smaller matrix that begins on the top left corner.
# i.e. find element x in the top left 1x1, 2x2, 3x3 matrix etc. In this case,
# the bottom-left most element in each of the matricies is the maximum element.
# i.e. the maximum element in the 1x1 matrix is array[1][1], and in the
# 2x2 its array[2][2].
# Now, we can iterate across the diagonal elements, if the target is less than
# the current diagonal, increment to the next diagonal ( array[i+1][i+1] ). If the
# target is less than the diagonal element, since it was greater than the previous
# diagonal element, we know it must lie in the row i or column i.

# extend this to the full problem by incrementing the row and column individually.
# use binary search to search in the individual row and column.

# RUN TIME ANALYSIS
# In the worst case, checking each diagonal will take O( m + n), and the single
# binary search will take O( log(n) ) time. Hence, this program will take O(m + n)
# time, or linear time.

def searchMatrix(arr, target):
    i = 0
    j = 0
    while i != len(arr) and j != len(arr[0]):
        if arr[i][j] == target:
            return True
        if arr[i][j] < target:
            #increment diagonally, if possible
            if arr[i+1]:
                i += 1
            if arr[i][j+1]:
                j +=1
            continue
        if arr[i][j] > target:
            column = []
            for row in range(len(arr)):
                column.append(arr[row][j])
            return binarySearch(arr[i], target) or binarySearch(column, target)
import math
def binarySearch(arr, target):
    mid = math.floor(len(arr)/2)
    if not arr:
        return None
    if arr[mid] == target:
        return True
    if arr[mid] > target:
        #check bottom half
        return binarySearch(arr[0:mid], target)
    if arr[mid] < target:
        return binarySearch(arr[mid: len(arr)-1], target)

arr = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(searchMatrix(arr, 24));
