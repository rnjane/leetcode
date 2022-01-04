"""
Given a string s, return the longest palindromic substring in s.
"""
class Solution:
    """
    - a palindrome can be identified by expanding from its center.(for odd numbered palindromes)
    1. starting from index 1 to second last index:
        - try checking if elements on either sides of the current index are equal.
        - if equal:
            record this as a palindrome.
            continue until they are not, or you runout of characters
            if the recorded palindrome is bigger than the current biggest, assign it as current_big
        - if not:
            continue
    2. starting from index 0 to second last index:(for even numbered palindromes)
        - check if current_index is equal to next element.
        - if equal:
            expand outwards until it is not, or you run out of elements, while recording the palindrome
        - if not:
            continue
    """
    def isPalindrome(self, string):
        left = 0
        right = len(string) - 1
        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def longestPalindrome(self, ins):
        if len(ins) <= 2:
            if len(ins) == 1:
                return ins
            elif len(ins) == 2:
                if self.isPalindrome(ins):
                    return ins
                else:
                    return ins[0]


        longest_palindromic_substring = ins[0]
        for index, _ in enumerate(ins):
            # this is to check for a palindrome of an odd length
            left = index - 1
            right = index + 1

            if index == 0 or index == len(ins) - 1:
                continue
            else:
                while ins[left] == ins[right]:
                    if len(longest_palindromic_substring) < right - left:
                        longest_palindromic_substring = ins[left:right+1]
                    left -= 1
                    right += 1
                    if left < 0 or right > len(ins) - 1:
                        break

        longest_palindromic_substring2 = ins[0]

        for index, _ in enumerate(ins):
            # this is to check for a palindrome of an even length
            left = index
            right = index + 1
            if index == len(ins) - 1:
                continue

            while ins[left] == ins[right]:
                if len(longest_palindromic_substring2) < (right - left) + 1:
                    longest_palindromic_substring2 = ins[left:right+1]
                left -= 1
                right += 1
                if left < 0 or right > len(ins) - 1:
                    break
        if len(longest_palindromic_substring2) > len(longest_palindromic_substring):
            longest_palindromic_substring = longest_palindromic_substring2


        return longest_palindromic_substring