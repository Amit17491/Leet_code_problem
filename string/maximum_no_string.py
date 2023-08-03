'''
You are given a 0-indexed array words consisting of distinct strings.

The string words[i] can be paired with the string words[j] if:

    The string words[i] is equal to the reversed string of words[j].
    0 <= i < j < words.length.

Return the maximum number of pairs that can be formed from the array words.

Note that each string can belong in at most one pair.

 

Example 1:

Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.
'''

from typing import List
def maximumNumberOfStringPairs(words: List[str]) -> int:
    num = []
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] == words[j][::-1]:
                if words[i] != words[j]:
                    num.append((i,j))
    if len(num) < 1:
        return 0
    else:
        x = len(num)
        return x//2



words = ["cd","ac","dc","ca","zz"]
print(maximumNumberOfStringPairs(words))