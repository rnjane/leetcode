"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
class Solution:
    # recusrsive solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

"""
1. create an empty stack and an empty list to hold traversed values.
2. assign root node to a variable current.
3. while stack is not empty or current is not None:
    while current is not None:
        add current to the stack
        assign current to current.left
    assign current to stack.pop()
    add current.val to return list
    assign current to current.right
"""
class Solution:
    # iterative solution
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        return_list = []
        current_node = root
        while stack != [] or current_node is not None:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            return_list.append(current_node.val)
            current_node = current_node.right
        return return_list