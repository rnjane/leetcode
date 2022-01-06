"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
class Solution:
    """
    1. create an empty queue, init current_node to root and add it to the queue.
    2. create a var level to denote the level we're at. init it to 0
    3. while queue is not empty:
        - add an empty list to our return_list
        - go through the current elements in the queue, popping them, adding them to their respective level and
            adding their left and right nodes.

    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = []
        return_array = []
        current_node = root
        level = 0
        queue.append(current_node)
        while queue:
            return_array.append([])
            for i in range(len(queue)):
                current_node = queue.pop(0)
                return_array[level].append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            level += 1
        return return_array

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels

"""
Both ways have O(n) space and time
"""