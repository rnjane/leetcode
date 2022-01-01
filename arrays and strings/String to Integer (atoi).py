"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
class Solution:
    """
    1. if first charcter is a space, continue until it is not.
    2. if the first charcter is not +/- or a number, return 0
    3. if it is a sign, record it in a variable.
    4. continue looping, until you encounter a non-numeric.
    - compute an int of the recorded value, with the appropriate sign applied.
    5. Check if it is within int boundaries and return as necessary.
    """
    def myAtoi(self, s: str) -> int:
        # 1. if first charcter is a space, continue until it is not.
        stripped_string = s.strip()

        # 2. if the first charcter is not +/- or a number, return 0
        if not stripped_string:
            return 0
        

        # 3. if it is a sign, record it in a variable.
        sign = 1
        if stripped_string[0] == '-':
            sign = -1
            stripped_string = stripped_string[1:]
        elif stripped_string[0] == '+':
            stripped_string = stripped_string[1:]
        
        # 4. continue looping, until you encounter a non-numeric.
        result = 0
        for char in stripped_string:
            # if the character is not a number, break. else, add it to the result.
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # 5. Check if it is within int boundaries and return as necessary. 
        result *= sign
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        return result
        