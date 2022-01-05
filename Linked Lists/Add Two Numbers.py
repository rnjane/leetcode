"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
class Solution:
    """
    the head of each node represents the ones(place value) of the number
    we start from both heads, and proceed in the linked list, until we get to the ends.
    if one number is larger than the other, we us 0 for digits missing
    we keep track of carry along the way
    """
    """
    1. create var carry and init it to 0. create an empty l.list
    2. while any of the lists still has values and there's no carry:
        get top vals of both lists and add them and add carry to them
        - if sum > 9:
            carry = sum // 10
            val = sum % 10
        add sum as a node to the new l.list.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return_linked_list = ListNode()
        current_node = return_linked_list
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum = val1 + val2 + carry
            if sum > 9:
                carry = sum // 10
                val = sum % 10
            else:
                carry = 0
                val = sum
            current_node.next = ListNode(val)
            current_node = current_node.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return return_linked_list.next

"""
Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.
"""