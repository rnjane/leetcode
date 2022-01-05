"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 
Follow up: Could you solve it without reversing the input lists?
"""
class Solution:
    """
    1. reverse the linked lists
    2. loop through both the lists, adding corresponding elements.
    3. as long as either list is not empty or there is a carry, continue addition. record the sum in a new linked list.
    4. return the linked list with the sums of the corresponding elements.
    """
    def reverseLinkedList(self, head):
        """
        1. create a var 'last' to hold the end of the l.list. init it to None
        2. while head:
            - old_next = head.next
            - head.next = last
            - last = head
            - head = old_next
            - return head
        """
        last = None
        while head:
            old_next = head.next
            head.next = last
            last = head
            head = old_next
        return last


    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseLinkedList(l1)
        l2 = self.reverseLinkedList(l2)
        """
        1. loop through both lists.
        2. while either of the lists is not empty, add corrsponding elements.
        3. if one of the lists does not have a corresponding element, use 0.
        4. if the sum is > 9, use a carry.
        5. add sums to a linked list, which will be returned.
        6. if there is a carry, continnue with the execution.
        """
        carry = 0
        return_linked_list = ListNode()
        current_node = return_linked_list
        while l1 or l2 or carry > 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            current_sum = l1_value + l2_value + carry
            if current_sum > 9:
                carry = current_sum // 10
                current_sum = current_sum % 10
            else:
                carry = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current_node.next = ListNode(current_sum)
            current_node = current_node.next
        return self.reverseLinkedList(return_linked_list.next)

"""
time complexity: 0(N1 + N2) where N1 and N2 is the number of elements in l1 and l2 respectively.
space complexity: 0(1) without taking the output list into consideration. 0(max(N1, N2)) with taking the output list into consideration.
"""