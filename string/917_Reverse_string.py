'''

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

'''


def reverseOnlyLetters(s: str) -> str:
    out = list(s)
    l = 0
    r = len(s)-1
    while r > -1:
        if s[r].isalpha():
            if out[l].isalpha():
                out[l] = s[r]
                r = r - 1
                l = l + 1
            else:
                l = l + 1
        else:
            r = r -1

    x = "".join(out)
    return x

s = "ab-cd"
print(reverseOnlyLetters(s))