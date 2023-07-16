'''
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
'''

from typing import List
def countWords(words1: List[str], words2: List[str]) -> int:
    num =[]
    s = words1 + words2
    for i in words1:
        if i in words2:
            num.append((s.count(i),i))

    lst = []
    for key, value in num:
        if key == 2:
            lst.append(value)

    count = 0
    for i in lst:
        count = count + 1 
    return count

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(countWords(words1, words2))