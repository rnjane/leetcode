"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
class Solution:
    """
    1. set four pointers, to denote top, bottom, left and right.
    2. set four vars to denote direction.
    3. move top to right adding all the vals.
    4. move top and right accordingly. then move top to bottom adding vals.
    5. move bottom and right accordingly and continue until top = bottom and
        left = right
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        direction = 0
        result = []
        while top <= bottom and left <= right:
            if direction == 0:
                if left == right + 1:
                    result.append(matrix[top][left])
                    top += 1
                    direction = 1
                else:
                    for i in range(left, right + 1):
                        result.append(matrix[top][i])
                    top += 1
                    direction = 1
            elif direction == 1:
                if top == bottom + 1:
                    result.append(matrix[top][left])
                    left += 1
                    direction = 2
                else:
                    for i in range(top, bottom + 1):
                        result.append(matrix[i][right])
                    right -= 1
                    direction = 2
            elif direction == 2:
                if left == right + 1:
                    result.append(matrix[top][left])
                    bottom -= 1
                    direction = 3
                else:
                    for i in range(left, right + 1)[::-1]:
                        result.append(matrix[bottom][i])
                    bottom -= 1
                    direction = 3
            elif direction == 3:
                if top == bottom + 1:
                    result.append(matrix[top][left])
                    right -= 1
                    direction = 0
                else:
                    for i in range(top, bottom + 1)[::-1]:
                        result.append(matrix[i][left])
                    left += 1
                    direction = 0
        return result

"""
time complexity: O(m*n) - we loop horizontally and vertically through the array once. 
space complexity: O(m*n) - we create a new matrix to store the result.
"""