'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 

'''

def secondHighest(s: str) -> int:
        num = []
        for i in s:
            if i.isdigit():
                if i in num:
                    continue
                else:
                    num.append(i)
        if len(num) > 1:
            x = sorted(num)
            return int("".join(x[-2]))
        else:
            return -1

s = "dfa12321afd"
print(secondHighest(s))