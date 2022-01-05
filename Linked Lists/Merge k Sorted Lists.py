"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
class Solution:
    """
    iterative solution - most efficient
    """
    def merge_2_sorted_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy_node = ListNode
        current_node = dummy_node
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        current_node.next = l1 if l1 is not None else l2
        return dummy_node.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        1. create a method to merge two l.lists
        2. merge the lists in the input list two by two until there is only one list
        """
        while len(lists) > 1:
            temp_list = []
            for i in range(0, len(lists), 2):
                if i != len(lists) - 1:
                    combined = self.merge_2_sorted_lists(lists[i], lists[i + 1])
                    temp_list.append(combined)
                else:
                    combined = lists[i]
                    temp_list.append(combined)
            lists = temp_list
        if lists == []:
            empty_node = ListNode()
            return empty_node.next
        else:
            return lists[0]

"""
ime complexity : O(Nlogk) where k is the number of linked lists.
- We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists. since we are halving input every time, we get to log(k) steps.
Space complexity : O(1)
"""


class Solution:
    """
    recursive solution - not efficient
    """
    def mergeTwoSortedLists(self, linked_list_1, linked_list_2):
        if not linked_list_1:
            return linked_list_2
        if not linked_list_2:
            return linked_list_1
        if linked_list_1.val < linked_list_2.val:
            linked_list_1.next = self.mergeTwoSortedLists(linked_list_1.next, linked_list_2)
            return linked_list_1
        else:
            linked_list_2.next = self.mergeTwoSortedLists(linked_list_1, linked_list_2.next)
            return linked_list_2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        1. create a method to merge two linked lists.
        2. merge the linked lists two by two until there is only one list
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.mergeTwoSortedLists(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))
