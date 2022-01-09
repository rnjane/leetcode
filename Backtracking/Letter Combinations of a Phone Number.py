"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution:
    """
    there is not an effctive way to solve this per say. we use backtracking to find all possible combinations.
    """
    def letterCombinations(self, digits: str):
        if digits == "":
            return []

        letter_mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        letter_collections = []
        for digit in digits:
            letter_collections.append(letter_mapping[str(digit)])
        # letter_collections will be ['abc', 'def'] for imput of 23

        if len(digits) == 1:
            return [x for x in letter_mapping[str(digit)]]
        # if input is 2, this'd return ["a","b","c"]
        

        # pop top collection(['abc']), and assign individual characters to top_collection_list
        top_collection = letter_collections.pop(0)
        top_collection_list = [x for x in letter_collections.pop(0)]

        # go through others in the letter collection
        for index, letter_collection in enumerate(letter_collections):
            coll = []
            letter_collection_list = [y for y in letter_collection]

            for ele in top_collection_list:
                for ele2 in letter_collection_list:
                    coll.append(ele + ele2)
            
            # to reduce memory usage, we replace the old value in letter_collections with the newly calculated value
            letter_collections[index] = coll

            # us the latest combination as the basis of other combinations
            top_collection_list = coll
        
        # the last element in letter_collections will represent the final combination we are looking for
        return letter_collections[-1]
                

sl = Solution()
print(sl.letterCombinations("2345"))

"""
Complexity Analysis

Time complexity: O(4^N . N), where N is the length of digits. Note that 4 in this expression is referring to the maximum value length in the hash map, and not to the length of the input.

The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. 
Then, for each combination, it costs up to N to build the combination. This problem can be generalized to a scenario where numbers correspond with up to MM digits, 
in which case the time complexity would be O(M^N \cdot N)O(M 
N
 ⋅N). For the problem constraints, we're given, M = 4M=4, because of digits 7 and 9 having 4 letters each.

Space complexity: O(N)O(N), where NN is the length of digits.

Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. 
It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.

As the hash map does not grow as the inputs grows, it occupies O(1)O(1) space.


"""