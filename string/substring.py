'''
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
'''
<<<<<<< HEAD
from typing import List
def numOfStrings(patterns: List[str], word: str) -> int:
    count = 0
    for item in patterns:
        if item in word:
            count = count + 1
    return count

patterns = ["a","abc","bc","d"]
word = "abc"
print(numOfStrings(patterns, word))
 
=======

from typing import List
def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for item in patterns:
            if item in word:
                count =  count + 1
        return count

patterns = ["a","abc","bc","d"]
word = "abc"
print(numOfStrings(patterns, word))
>>>>>>> 1697f82 (misssing solution from day4)
