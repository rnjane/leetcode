"""
create a set to hold visited nodes. for every element in the matrix, if the column is valid, and the row is valid,
and the element if not in the visited nodes set and the value corresponds to the current character in our searched word,
- add it to the set
- recursively perform dfs on all sides, and if any returns true, return true, else False
- remove the node from the set
"""



"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:

    """
    loop through the matrix
    perform dfs of every element in the matrix, in all directions trying to find the searched word. return true if found.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_of_rows = len(board)
        num_of_columns = len(board[0])
        visited_nodes_set = set()

        def dfs(row, column, index_of_current_character_in_the_searched_word):
            if index_of_current_character_in_the_searched_word == len(word):
                return True
            else:
                if (
                    row < 0 or column < 0 or row >= num_of_rows
                    or column >= num_of_columns or
                    word[index_of_current_character_in_the_searched_word] != board[row][column] or
                    (row, column) in visited_nodes_set
                    ):
                    return False
                else:
                    visited_nodes_set.add((row, column))
                    backtrack_result = dfs(
                        dfs(row + 1, column, index_of_current_character_in_the_searched_word + 1) or
                        dfs(row - 1, column, index_of_current_character_in_the_searched_word + 1) or
                        dfs(row, column + 1, index_of_current_character_in_the_searched_word + 1) or
                        dfs(row, column - 1, index_of_current_character_in_the_searched_word + 1)
                    )
                    # we remove so that the next element to be visited can add the same element
                    visited_nodes_set.remove((row, column))
                    return backtrack_result

        for row_index in range(num_of_rows):
            for column_index in range(num_of_columns):
                if dfs(row_index, column_index, 0):
                    return True
        return False

"""Time complexity => O(num_of_rows * num_of_columns * 4^n)
4 ^ n is for the dfs recursion
the other od for the nnested loop"""