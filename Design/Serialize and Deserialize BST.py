"""
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You need to ensure that a binary search tree can be serialized to a string, 
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    serialize.
    - go through the tree using dfs. base case is when a null Node is found, at ehich point we add a
        designated character to our serialized nodes list. else, we add the node, and recursivele
        dfs left and then right(pre-order)

    deserialize.
    - split the input by comma, or whichever delimiter was used.
    - initialize current_index to 0, it will track our index in the split list.
    - if the current value is None, we increment current_index and returnn None
    - else:
        - we create a new node with the current_node value
        - increment current_index
        - assign the new node's left to dfs() and same for the right node.
        - we return this node
    return a call to dfs()
    """
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        serialized_nodes = []
        def dfs(node):
            if not node:
                serialized_nodes.append("None")
                return
            else:
                serialized_nodes.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(serialized_nodes)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        serialized_values = data.split(",")
        self.current_index = 0

        def dfs():
            if serialized_values[self.current_index] == "None":
                self.current_index += 1
                return None
            else:
                node = TreeNode(int(serialized_values[self.current_index]))
                self.current_index += 1
                node.left = dfs()
                node.right = dfs()
                return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans