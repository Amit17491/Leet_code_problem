'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"

Example 2:

Input: n = 1234
Output: "1.234"

'''

def thousandSeparator(n: int) -> str:
    s = str(n)
    res =""
    count = 0
    for ch in s[::-1]:
        if count == 3:
            res = res + '.'
            count = 0
        res = res + ch
        count = count + 1
    return res[::-1]

n = 1234
print(thousandSeparator(n))