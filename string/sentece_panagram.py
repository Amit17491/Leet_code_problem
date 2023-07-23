'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
'''

def checkIfPangram(sentence: str) -> bool:
    l = "abcdefghijklmnopqrstuvwxyz"
    return True if len(set(sentence)) == len(l) else False

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))
