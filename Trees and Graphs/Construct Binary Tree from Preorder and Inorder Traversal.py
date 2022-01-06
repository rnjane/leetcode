# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # Recursive solution
        if inorder:   
            # Find index of root node within in-order traversal
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            
            # Recursively generate left subtree starting from 
            # 0th index to root index within in-order traversal
            root.left = self.buildTree(preorder, inorder[:index])
            
            # Recursively generate right subtree starting from 
            # next of root index till last index
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root




class Solution:
    """
    Preorder traversal follows Root -> Left -> Right
    Inorder traversal follows Left -> Root -> Right
    - the first element in the pre-order will be the root.
    - having found the root, divide post-order array into left and right sub trees.
    - recursively repeat the process for each sub-tree.
    """
    """

    Preorder traversal follows Root -> Left -> Right, therefore, given the preorder array preorder,
    we have easy access to the root which is preorder[0].

    Inorder traversal follows Left -> Root -> Right, therefore if we know the position of Root,
    we can recursively split the entire array into two subtrees.

    recursivr fxn:
    it will set the first element of preorder as the root, and then construct the entire tree.
    To find the left and right subtrees, it will look for the root in inorder,
    so that everything on the left should be the left subtree, and everything on the right should be the right subtree.
    Both subtrees can be constructed by making another recursion call.

    It is worth noting that, while we recursively construct the subtrees,
    we should choose the next element in preorder to initialize as the new roots.
    This is because the current one has already been initialized to a parent node for the subtrees.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid_point = inorder.index(preorder[0])

        # Recursively generate left subtree starting from 
        # 0th index to root index within in-order traversal
        root.left = self.buildTree(preorder[1:mid_point + 1], inorder[:mid_point])

        # Recursively generate right subtree starting from 
        # next of root index till last index
        root.right = self.buildTree(preorder[mid_point + 1:], inorder[mid_point + 1:])

        return root

"""
Complexity analysis

Let NN be the length of the input arrays.

Time complexity : O(N)O(N).

Building the hashmap takes O(N)O(N) time, as there are NN nodes to add, and adding items to a hashmap has a cost of O(1)O(1), so we get N \cdot O(1) = O(N)N⋅O(1)=O(N).

Building the tree also takes O(N)O(N) time. The recursive helper method has a cost of O(1)O(1) for each call (it has no loops), and it is called once for each of the NN nodes, giving a total of O(N)O(N).

Taking both into consideration, the time complexity is O(N)O(N).

Space complexity : O(N)O(N).

Building the hashmap and storing the entire tree each requires O(N)O(N) memory. The size of the implicit system stack used by recursion calls depends on the height of the tree, which is O(N)O(N) in the worst case and O(\log N)O(logN) on average. Taking both into consideration, the space complexity is O(N)O(N).
"""

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # Recursive solution
        if inorder:   
            # Find index of root node within in-order traversal
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            
            # Recursively generate left subtree starting from 
            # 0th index to root index within in-order traversal
            root.left = self.buildTree(preorder, inorder[:index])
            
            # Recursively generate right subtree starting from 
            # next of root index till last index
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root