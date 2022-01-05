"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        1. Two pointers, slow and fast.
        2. slow moves 1 step each time, fast moves 2 steps each time.
        3. If there is a cycle, fast will eventually meet slow.
        4. If there is no cycle, fast will never meet slow.
        """
        if head is None:
            return False
        pointer_1 = head
        pointer_2 = head.next
        while pointer_1 is not None and pointer_2 is not None:
            if pointer_1 == pointer_2:
                return True
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
            if pointer_2 is not None:
                pointer_2 = pointer_2.next
        return False
