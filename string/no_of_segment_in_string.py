'''
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

'''

def countSegments(s: str) -> int:
    s = s.split()
    return len(s)

s = "Hello, my name is John"
print(countSegments(s))