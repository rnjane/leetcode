"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
"""

class Solution:
    """
    1. calculate the length of both linked lists.
    2. create two pointers, one points at the beginning of the smaller list.
    - the other points at the index of difference of legths of the two lists, in the larger list.
    3. move the two pointers forward until they point to the same node.
    """
    def getLinkedListLength(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_a = self.getLinkedListLength(head=headA)
        length_b = self.getLinkedListLength(head=headB)
        if length_a > length_b:
            pointer_1 = headB
            nodes_difference = length_a - length_b
            start = headA
            for i in range(nodes_difference):
                start = start.next
            pointer_2 = start
        else:
            pointer_1 = headA
            nodes_difference = length_b - length_a
            start = headB
            for i in range(nodes_difference):
                start = start.next
            pointer_2= start
        while True:
            if pointer_1 is None and pointer_2 is None:
                return None
            elif pointer_1 is not pointer_2:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next
            else:
                return pointer_1