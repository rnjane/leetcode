"""
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
"""
class Solution:
    def reverse_list(self, ls, start_index, end_index):
        pointer_1 = start_index
        pointer_2 = end_index
        while pointer_2 >= pointer_1:
            ls[pointer_1], ls[pointer_2] = ls[pointer_2], ls[pointer_1]
            pointer_1 += 1
            pointer_2 -= 1

    def reverseWords(self, s):
        """
        1. reverse the entire list
        2. reverse individual words
        """
        self.reverse_list(s, 0, len(s) - 1)
        word_start = 0
        word_end = 0
        
        for index, character in enumerate(s):
            if index == len(s) - 1:
                self.reverse_list(s, word_start, word_end)
                break
                # print((s[word_start], s[word_end]))
            if character != " ":
                word_end += 1
            elif character == " ":
                self.reverse_list(s, word_start, word_end - 1)
                word_end += 1
                word_start = word_end
        