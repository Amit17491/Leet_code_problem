'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

'''

def halvesAreAlike(s: str) -> bool:
    s = s.lower()
    l = len(s)//2
    A = s[:l]
    B = s[l:]
    l = ['a', 'e', 'i', 'o', 'u']
    acount = 0
    bcount = 0
    for i in A:
        if i in l:
            acount = acount + 1
    
    for i in B:
        if i in l:
            bcount = bcount + 1

    if acount == bcount:
        return True
    else:
        return False

s = "book"
print(halvesAreAlike(s))