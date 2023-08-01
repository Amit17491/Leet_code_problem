'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

'''

from typing import List
def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    lst = []
    s1 = s1.split()
    s2 = s2.split()

    s = s1 + s2
    for i in s:
        x = s.count(i)
        lst.append((i,x))

    x = dict(lst)
    num = []
    for key, value in x.items():
        if value == 1:
            num.append(key)
    return num

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))