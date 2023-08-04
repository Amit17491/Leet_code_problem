'''

Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

'''
from typing import List
def findOcurrences(text: str, first: str, second: str) -> List[str]:
    text = text.split()
    num = []
    for i in range(len(text)-1,1, -1):
        if text[i-1] == second and text[i-2] == first:
            num.append(text[i])
        else:
            continue
    return num[::-1]
text = "alice is a good girl she is a good student"
first = "a" 
second = "good"

print(findOcurrences(text, first, second))
