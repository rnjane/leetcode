"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
# BEST SOLUTION HERE
class Solution:
    """
    Algorithm

    - first, confirm root is not none.
    - if it is not either of the search values, search its right and left(recursively)
    - contnue until you find a node we are searching for. when found, return it.
    - 
    """
    def lowestCommonAncestor(self, root, p, q):
        def lca(p, q, root):
            if not root:
                return False
            
            if root == p or root == q:
                return root
            
            left = lca(p, q, root.left)
            right = lca(p, q, root.right)
            
            if left and right:
                return root
            
            # if both of them are not true, return whichever one is true
            if left:
                return left
            else:
                return right
                
        return lca(p, q, root)


"""
recursive
Complexity Analysis

Time Complexity: O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed binary tree could be N.
"""