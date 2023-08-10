'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

    Each substring is balanced.

Return the maximum number of balanced strings you can obtain.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

'''

def balancedStringSplit(s: str) -> int:
    num = []
    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'L':
            count  = count + 1
            if count == 0:
                num.append(count)
        else:
            count =  count - 1
            if count == 0:
                num.append(count)
    return len(num)

s = "RLRRLLRLRL"
print(balancedStringSplit(s))
