"""
Given n non-negative intwhiegers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution():
    """
    the amount of trapped water by every building is the minimum of highest left and right side 'walls' less the height of that building.
    we calculate amount of trapped water by every building by looping through the array and keeping track of the highest left and right side 'walls'.
    right_max and left_max are the highest left and right side 'walls' of the current building.
    trapped_water is the amount of water trapped by the current building.
    left_pointer and right_pointer are the left and right side pointers of the current building.
    while left_pointer < right_pointer, we keep looping through the array and keep track of the highest left and right side 'walls'.
        if the height of the current building is less than the height of the left side 'wall', 
            we update left_max to be the height of the current building.
        if the height of the current building is less than the height of the right side 'wall', 
            we update right_max to be the height of the current building.
        if the height of the current building is greater than the height of the left side 'wall', 
            we update trapped_water by adding the difference between left_max and the height of the current building.
        if the height of the current building is greater than the height of the right side 'wall', 
            we update trapped_water by adding the difference between right_max and the height of the current building.
    """
    def trap(self, height):
        left_max = 0
        right_max = 0
        trapped_water = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                if height[left_pointer] > left_max:
                    left_max = height[left_pointer]
                else:
                    trapped_water += left_max - height[left_pointer]
                left_pointer += 1
            else:
                if height[right_pointer] > right_max:
                    right_max = height[right_pointer]
                else:
                    trapped_water += right_max - height[right_pointer]
                right_pointer -= 1
        return trapped_water

"""
time complexity: O(n) - we loop through the array once to calculate the amount of trapped water by every building.
space complexity: O(1) - we don't use any extra space to solve this problem.
"""