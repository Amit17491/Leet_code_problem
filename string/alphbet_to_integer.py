'''
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

'''


def freqAlphabets(s: str) -> str:
    i = len(s) -1
    decode = ""
    while  i >= 0:
        if s[i] == '#':
            num = s[i-2:i]
            decode = decode + chr(ord('a') + int(num) -1)
            i -=3
        else:
            decode = decode + chr(ord('a') + int(s[i]) -1)
            i = i - 1
    return decode[::-1]

s = "10#11#12"
print(freqAlphabets(s))