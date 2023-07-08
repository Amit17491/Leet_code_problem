'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
'''

def toLowerCase(s: str) -> str:
    return s.lower()

s = "Hello"
print(toLowerCase(s))