'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
'''
from typing import List
def firstPalindrome(words: List[str]) -> str:
        for item in words:
            if item[:] == item[::-1]:
                return item
        return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))