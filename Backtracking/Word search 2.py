"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
"""
class TrieNode:
    """
    A trie node id defined by its children and a variable indicating of it is the end of a word.
    """
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        current = self
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.isWord = True

class Solution:
    """
    add all the words to a trie
    go through every element of the baord, and perform a recursive dfs on all possible directions. 
    At each call, we check if the sequence of letters that we traverse so far matches any word in the trie, with the help of the Trie data structure that we built at the beginning.
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        num_of_rows = len(board)
        num_of_columns = len(board[0])

        found_words_set = set()
        visited_elements_set = set()

        def dfs(row, column, node, word):
            #this if statement is our base case, if hit, we end the recursive calls
            if(row < 0 or column < 0 or row == num_of_rows or column == num_of_columns
                or board[row][column] not in node.children or (row, column)
                in visited_elements_set):
                return

            #add the element to the set so we can not visit it again
            visited_elements_set.add((row, column))

            #get the child of the passed node with the current element(character)
            node = node.children[board[row][column]]

            #append the character to our word
            word += board[row][column]

            #check if we're at word end, if so, add our word to the set
            if node.isWord:
                #suggestion: remove word from the Trie
                found_words_set.add(word)

            #recursive case, go through all the possibilities
            dfs(row + 1, column, node, word)
            dfs(row - 1, column, node, word)
            dfs(row, column + 1, node, word)
            dfs(row, column - 1, node, word)

            #when all the possibilities have been explored, remove the row and column from the set ready for the next element in the nested loops.
            visited_elements_set.remove((row, column))

        for row_index in range(num_of_rows):
            for column_index in range(num_of_columns):
                dfs(row_index, column_index, root, "")

        return list(found_words_set)


"""O(M(4⋅3 ^ L−1))
M - (r * c) we're going through every element in the matrix
4 - possible directions we can go from a certain element
3 - possible directions we can go moving forward
L - 1 - l is the max len of words """