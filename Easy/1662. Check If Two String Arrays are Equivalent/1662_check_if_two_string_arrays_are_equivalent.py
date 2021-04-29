"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true

Explanation:

word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""

# THOUGHTS
# This problem wasn't too bad. 
# My biggest issues were remembering proper Python syntax, especially how to use 
#   the join() function and ternary operators.
# The problem specified that the arrays were string arrays, but maybe one thing I 
#   ask in a real interview is if the array could contain non-string elements.

# ------------- ATTEMPT 1
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        This function checks if two lists of strings create the same string when their 
        elements are concatenated together in order.

        This function runs in O(n+m), where n is length of the word1 array 
        and m is the length of the word2 array.

        Space complexity is O(1), since only strings needed to be stored.
        """
        first_word = "".join(word1)
        sec_word = "".join(word2)
        
        return True if first_word == sec_word else False