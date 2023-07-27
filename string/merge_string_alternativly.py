'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

'''

def mergeAlternately(word1: str, word2: str) -> str:
    lst = []
    for x in range(max(len(word1), len(word2))):
        lst.append(word1[x] if x < len(word1) else "")
        lst.append(word2[x] if x < len(word2) else "")
    result = ''.join(lst)
    return result

word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))

