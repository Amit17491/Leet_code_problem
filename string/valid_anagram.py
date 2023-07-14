'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
'''

def isAnagram(s: str, t: str) -> bool:
        s1 = list(s)
        t1 = list(t)
        if sorted(s1) == sorted(t1):
            return True
        else:
            return False

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))