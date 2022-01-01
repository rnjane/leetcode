"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    """
    - create a dict to hold difference between target and nums[i].
    - iterate through nums, if nums[i] is in dict, return the index of nums[i] and i. if it is not, add nums[i] to dict.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences_dictionary = {}
        for i in range(len(nums)):
            if nums[i] in differences_dictionary:
                return [differences_dictionary[nums[i]], i]
            else:
                differences_dictionary[target - nums[i]] = i

"""
Complexity.
- Time is O(n) - we are looping through all elements
- Space is O(n) - for the dict
"""