'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).


Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

'''

def areOccurrencesEqual(s: str) -> bool:
    num = []
    for i in s:
        x = s.count(i)
        if x in num:
            continue
        else:
            num.append((x))

    y = sorted(list(set(num)))
    if len(y)>1:
        return False
    else:
        return True

s = "abacbc"
print(areOccurrencesEqual(s))