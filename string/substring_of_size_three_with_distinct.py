'''
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

'''

def countGoodSubstrings(s: str) -> int:
    num = []
    j = len(s)
    l = 0
    r = 3
    while l < j:
        x  = s[l:r]
        l = l + 1
        r = r + 1
        if len(x) == 3:
            num.append(x)
        else:
            continue
    count = 0
    for i in num:
        if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
            continue
        else:
            count = count + 1
    return count


s = "xyzzaz"
print(countGoodSubstrings(s))