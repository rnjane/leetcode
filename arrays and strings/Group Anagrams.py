"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
class Solution:
    """
    - create an empty dict
    1. Loop through the list and sort each word.
    2. if the sorted word is not in the dict, add it and as a value,
        create a list with the original word.
    - if it is in the dict, append to its list the original word.
    - return all the values in the dict.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in sorted_words:
                sorted_words[sorted_word].append(word)
            else:
                sorted_words[sorted_word] = [word]
        return sorted_words.values()

"""
Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
Space complexity: O(n*k)
"""