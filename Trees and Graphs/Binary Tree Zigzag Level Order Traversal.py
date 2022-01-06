"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""
from collections import deque
class Solution:
    """
    1. create an empty queue, init current_node to root and add it to the queue.
    2. create a var level to denote the level we're at. init it to 0
    3. while queue is not empty:
        - add an empty list to our return_list
        - go through the current elements in the queue, popping them, adding them to their respective level and
            adding their left and right nodes.

    """
    """
    - the concept is using level order traversal with a var, left_to_right, to keep track of the direction
        to move.
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        left_to_right = True
        return_array = []
        queue = deque([root])
        level = 0
        while queue:
            return_array.append([])
            for i in range(len(queue)):
                if left_to_right:
                    current_value = queue.popleft()
                else:
                    current_value = queue.pop()
                return_array[level].append(current_value.val)

                if not left_to_right:
                    if current_value.right:
                        queue.appendleft(current_value.right)
                    if current_value.left:
                        queue.appendleft(current_value.left)
                else:
                    if current_value.left:
                        queue.append(current_value.left)
                    if current_value.right:
                        queue.append(current_value.right)

            left_to_right = not left_to_right
            level += 1

        return return_array


"""
Here we implement the DFS algorithm via recursion. 
We define a recursive function called DFS(node, level) which only takes care of the current node which is located at the 
specified level. Within the function, here are three steps that we would perform:

If this is the first time that we visit any node at the level, i.e. the deque for the level does not exist, 
then we simply create the deque with the current node value as the initial element.

If the deque for this level exists, then depending on the ordering, we insert the current node value either to the head or 
to the tail of the queue.

At the end, we recursively call the function for each of its child nodes.
"""

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode], level=0, levels=None) -> List[List[int]]:
        
        if not levels:
            levels = []
            
        if not root:
            return levels
            
        if len(levels) < level + 1:
            levels.append(deque([]))
            
        # Left -> Right
        if level % 2 == 0:
            levels[level].append(root.val)
        # Left <- Right
        else:
            levels[level].appendleft(root.val)
                
                
        self.zigzagLevelOrder(root.left, level + 1, levels)

        self.zigzagLevelOrder(root.right, level + 1, levels)
        
        return levels