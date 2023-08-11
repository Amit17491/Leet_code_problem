'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

'''


def firstUniqChar(s: str) -> int:
    for i in range(len(s)):
        x = s.count(s[i])
        if x == 1:
            return i
    return -1

s = "leetcode"
print(firstUniqChar(s))