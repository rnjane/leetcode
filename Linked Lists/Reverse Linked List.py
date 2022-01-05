"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class Solution:
    """
    1. Starting with the head:
    - keep record of the next node
    - point the next of head to previous node(initialized to None)
    - continue until current node is None
    
    1. create 3 vars, current, prev and next.
    2. current = head
    3. prev = null
    4. next = head.next_node
    5. while current is not None:
        head.next = prev
        prev = current
        current = next
        next = current.next
    return head
    """
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

"""
Time complexity: O(n) where n is the number of nodes in the list.
Space complexity: O(1) since we are not using any extra space.
"""