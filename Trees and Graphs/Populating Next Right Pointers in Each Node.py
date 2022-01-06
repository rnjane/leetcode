"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    """
    we use a queue
    we add elements to the queue level by level starting with the root node
    for every level, point each element to the next element in the queue, until you get to the end of that level
    """
    """
    - check if root is None. if it is, return it
    1. create an empty queue
    2. add the root to the queue
    3. while the queue is not empty:
        - take a snapshot of the current elements in the queue
        - pop them one at a time, and as long as it is not the last one,
            point next to the next element in the nodes_queue
        - if there's left and/or right, add them to the queue
    """
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = []
        queue.append(root)
        while queue:
            curr_len = len(queue)
            for i in range(curr_len):
                current_node = queue.pop(0)
                if i < curr_len - 1:
                    current_node.next = queue[0]
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return root

# resursive - less optimal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.mutate(root, None, None)
        return root
    
    def mutate(self, node, parent, isLeftChild):
        if node is None:
            return
        
        if parent is None:
            node.next = None
        elif isLeftChild:
            node.next = parent.right
        else:
            if parent.next is None:
                node.next = None
            else:
                node.next = parent.next.left
        
        self.mutate(node.left, node, True)
        self.mutate(node.right, node, False)