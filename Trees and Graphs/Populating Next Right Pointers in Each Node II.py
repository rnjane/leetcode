class Solution:
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