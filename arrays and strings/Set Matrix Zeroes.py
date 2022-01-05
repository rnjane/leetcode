"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution:
    """
    1. go through the rows, and if there is a zero, set the first element to 0.
    2. do the same for the columns.
    3. use a variable column_zero to denote when columns are 0(to not confuse with rows)
    """
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column_zero = False
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0

                    if column == 0:
                        column_zero = True
                    else:
                        matrix[0][column] = 0

        for row in range(1, len(matrix)):
            for column in range(1, len(matrix[0])):
                if matrix[row][0] == 0:
                    matrix[row][column] = 0
                
                if matrix[0][column] == 0:
                    matrix[row][column] = 0
        
        if matrix[0][0] == 0:
            for column in range(len(matrix[0])):
                matrix[0][column] = 0
        
        if column_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0

"""
time complexity: O(m*n) - we loop horizontally and vertically through the array once.
space complexity: O(1) - we don't use any extra space to solve this problem.
"""