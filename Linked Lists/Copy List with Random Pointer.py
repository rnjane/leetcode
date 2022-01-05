"""
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that 
the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 
Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""
class Solution:
    """
    1. create an empty node
    2. if l1.val < l2.val:
        empty_nnode.next = l1
        l1 = l1.next
    else:
        empty_nnode.next = l2
        l2 = l2.next
    3. empty_nnode = empty_nnode.next
    4. if l1 or l2 is not None:
        goto 2
    5. return empty_nnode.next
    

    """
    def copyLinkedList(self, head):
        current_node = head
        new_linked_list = Node
        current_new_node = new_linked_list
        while current_node is not None:
            new_node = Node(x=current_node.val)
            current_new_node.next = new_node
            current_node = current_node.next
            current_new_node = current_new_node.next
        return new_linked_list.next

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        linked_list_copy = self.copyLinkedList(head)
        old_list_order = []
        current_node = head
        current_new_node = linked_list_copy
        while current_node is not None:
            old_list_order.append(current_node)
            temp_next = current_node.next
            current_node.next = current_new_node
            current_node = temp_next
            if current_new_node:
                current_new_node = current_new_node.next
            else:
                current_new_node = None

        current_node = head
        current_new_node = linked_list_copy
        while current_new_node is not None:
            current_new_node.random = old_list_order.pop(0)
            current_new_node = current_new_node.next

        current_new_node = linked_list_copy
        while current_new_node is not None:
            if current_new_node.random.random:
                current_new_node.random = current_new_node.random.random.next
            else:
                current_new_node.random = None
            current_new_node = current_new_node.next

        return linked_list_copy