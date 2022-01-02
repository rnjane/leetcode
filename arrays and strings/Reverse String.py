"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    """
    1. create 2 pointers, one 0 and the other the length of the string.
    2. while pointer_1 is less than or equal to pointer_2:
        exchange the characters pointed at by the two arrays
        move right_pointer backwards
        move left_pointer forward
    """
    def reverseString(self, s: List[str]) -> None:
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer += 1
            right_pointer -= 1
            