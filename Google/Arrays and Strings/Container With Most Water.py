"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
"""
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""
class Solution:
    """
    we use two pointers to find the max area, one starting from the start and the other at the end of the array.
    the area between the two pointers is the product of the minimum of the two heights(where the pointers are at) and the distance between the pointers.
    we move the pointers towards each other until the distance between the pointers is 0.
        - all along, we re-compute the area between the two pointers and update max_area if the area is greater than max_area.
    """
    def maxArea(self, height) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_area


    def maxArea(self, height) -> int:
        res = 0 
        left = 0 
        right = len(height)-1
        while left < right:
            minHeight = min(height[left], height[right])
            res = max(res, minHeight * (right-left))
            while left < right and height[left] <= minHeight:
                left += 1 
            while left < right and height[right] <= minHeight:
                right -= 1
        return res