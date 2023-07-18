'''
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 

Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
'''
def percentageLetter(s: str, letter: str) -> int:
    for i in letter:
        x = s.count(i)
        x =  x/(len(s))*100
        return int(x)

s = "foobar"
letter = "o"
print(percentageLetter(s, letter))