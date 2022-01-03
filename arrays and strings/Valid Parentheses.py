"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    """
    1. create an empty stack.
    2. create a map(dict) of valid pair of parenthesis.
    3. loop through the input list:
        - if it is an opening, always add it to the stack.
        - if it is a closing and the stack is empty, return False
        - if it is a closing and the stack is not empty, and it does not match the element at the top of the stack, add it.
        - if it is a closing, and it matches the top element, pop the top
            element and continue
    4. If the stack is empty return True, else return False
    """
    def isValid(self, s):
        parenthesis_stack = []
        valid_pair = {"{": "}", "[": "]", "(": ")"}
        for character in s:
            if character in valid_pair:
                parenthesis_stack.append(character)
            elif parenthesis_stack and character == valid_pair[parenthesis_stack.pop()]:
                continue
            else:
                return False
        if parenthesis_stack == []:
            return True
        else:
            return False