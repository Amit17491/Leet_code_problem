'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
'''
<<<<<<< HEAD
from typing import List
def detectCapitalUse(word: str) -> bool:
    print(word[1:].lower())
    return word.isupper() or word.islower() or word[1:].lower() == word[1:]

word = "USA"
print(detectCapitalUse(word))

=======

from typing import List
def detectCapitalUse(word: str) -> bool:
    return word.isupper() or word.islower() or word[1:].lower() == word[1:]
word = "USA"
print(detectCapitalUse(word))
>>>>>>> 1697f82 (misssing solution from day4)
