'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

'''

def addStrings(num1: str, num2: str) -> str:
    #sys.set_int_max_str_digits(68000)  for the leetcode compiler.
    x = int(num1) 
    y = int(num2)
    return str(x + y)

num1 = "11"
num2 = "123"
print(addStrings(num1, num2))