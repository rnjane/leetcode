"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
import collections
class Solution:
    """
    Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search.
    During DFS, every visited node should be set as '0' to mark as visited node.
    Count the number of root nodes that trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_of_rows = len(grid)
        num_of_columns = len(grid[0])
        visited_set = set()

        num_of_islands = 0

        
        # don't start with this function, start with the for loop
        def bfs(row_index, column_index):
            queue = collections.deque()
            visited_set.add((row_index, column_index))
            queue.append((row_index, column_index))

            while queue:
                current_row, current_column = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for row_direction, column_direction in directions:
                    row, column = current_row + row_direction, current_column + column_direction
                    if (row in range(num_of_rows) and
                        column in range(num_of_columns) and
                        grid[row][column] == "1" and
                        (row, column) not in visited_set):
                        queue.append((row, column))
                        visited_set.add((row, column))


        for row_index in range(num_of_rows):
            for column_index in range(num_of_columns):
                if grid[row_index][column_index] == "1" and (row_index, column_index) not in visited_set:
                    bfs(row_index, column_index)
                    num_of_islands += 1

        

        return num_of_islands

"""
Complexity Analysis

Time complexity : O(M×N) where M is the number of rows and NN is the number of columns.

Space complexity : O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).
"""