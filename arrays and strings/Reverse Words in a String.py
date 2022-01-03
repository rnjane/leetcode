"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
class Solution:
    def reverseWords(self, input_string: str) -> str:
        """
        1. strip the input string(remove leading and trailing spaces)
        2. split the sentence using space.
        3. reverse the split words.
        4. join the split words using a space -> " ".join(sentence)
        """
        return " ".join(input_string.strip().split()[::-1])


class Solution:
    """
    1. strip the input string(remove leading and trailing spaces)
    2. split the sentence using space.
    3. reverse the split words.
    4. join the split words using a space -> " ".join(sentence)
    """
    def strip_string(self, input_string):
        pointer_1 = 0
        pointer_2 = len(input_string) - 1
        while input_string[pointer_1] == " ":
            pointer_1 += 1
        while input_string[pointer_2] == " ":
            pointer_2 -= 1

        return input_string[pointer_1:pointer_2+1]

    def split_string(self, input_string):
        return_list = []
        current_word = ""
        prev_space = False
        for index, character in enumerate(input_string):
            if character == " " and not prev_space:
                return_list.append(current_word)
                current_word = ""
                prev_space = True
            elif character == " " and prev_space:
                continue
            else:
                if index == len(input_string) - 1:
                    current_word += character
                    return_list.append(current_word)
                else:
                    current_word += character
                    prev_space = False
        return return_list

    def join_string(self, input_list, join_character):
        return_string = ""
        for index, word in enumerate(input_list):
            # for the last word, add it without adding the join_character
            if index == len(input_list) - 1:
                return_string += word
            else:
                return_string += word
                return_string += join_character
        return return_string


    def reverseWords(self, s: str) -> str:
        s = self.strip_string(s)
        s = self.split_string(s)
        s.reverse()
        return self.join_string(s, " ")
        