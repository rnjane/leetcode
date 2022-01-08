class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    """
    a trie is like an inverted tree: with the roots at the top.
    insert: for each word, check if the first letter is in the root. if it is, follow that path with the other letters.
    if it is not, create a new node with the first letter as the key, and follow that path with the other letters.

    search: for each word, check if the first letter is in the root. if it is, follow that path with the other letters.
    if it is not, return False.

    startsWith: for each word, check if the first letter is in the root. if it is, follow that path with the other letters.
    if it is not, return False.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.endOfWord = True


    def search(self, word: str) -> bool:
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            else:
                current = current.children[character]

        return current.endOfWord


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            else:
                current = current.children[character]

        return True