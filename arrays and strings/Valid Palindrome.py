"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    """
    Set two pointers, one at each end of the input string
    If the input is palindromic, both the pointers should point to equivalent characters, at all times.
    If this condition is not met at any point of time, we break and return early.
    We can simply ignore non-alphanumeric characters by continuing to traverse further.
    Continue traversing inwards until the pointers meet in the middle.
    """
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            # if we encounter a character that is not alphanumeric, we continue until we find one that is so, as lomg as left < right.
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1
            
            # check for equality of the characters at the two pointers
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            # move the pointers towards each other
            left_pointer += 1
            right_pointer -= 1
        return True
