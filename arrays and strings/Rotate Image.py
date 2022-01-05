"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
class Solution:
    """
    - the logic of 90 degree rotation is to transpose the matrix, then reverse the rows.
    1. transpose the matrix (swap rows and columns) and then reverse the rows.
    2. reverse the rows of the matrix (in place) by swapping the elements.
    - Time Complexity: O(N^2) where N is the length of the matrix. We transpose the matrix and reverse the rows.
    - Space Complexity: O(1) since we do not allocate any additional space.
    """
    def transpose_matrix(self, matrix):
        """
        transpose the matrix (swap rows and columns)
        """
        matrix_length = len(matrix)
        for row in range(matrix_length):
            for column in range(row, matrix_length):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        return matrix

    def reverse_rows(self, matrix):
        """
        reverse the rows of the matrix (in place) by swapping the elements.
        """
        matrix_length = len(matrix)
        for row in range(matrix_length):
            # reverse the row. [::-1] reverses the list.
            matrix[row] = matrix[row][::-1]
        return matrix

    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = self.transpose_matrix(matrix)
        matrix = self.reverse_rows(matrix)
        return matrix