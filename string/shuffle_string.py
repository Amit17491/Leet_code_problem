'''
1528. Shuffle String
Easy
2.4K
424
Companies
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

'''
from typing import List
def restoreString(s: str, indices: List[int]) -> str:
        s = list(s)
        num = [' '] * len(s)
        for item in range(len(s)):
            num[indices[item]] = s[item]
        x = "".join(num)
        return x

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))







