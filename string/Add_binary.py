'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
'''
"Note figure out these question"
def addBinary(a: str, b: str) -> str:
    return bin(int(a,2) + int(b,2))[2:]

a = "11"  
b = "1"
print(addBinary(a,b))