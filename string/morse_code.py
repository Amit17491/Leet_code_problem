'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

    'a' maps to ".-",
    'b' maps to "-...",
    'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.

Return the number of different transformations among all words we have.

 

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

'''
from typing import List
def uniqueMorseRepresentations(words: List[str]) -> int:
    alpha = [chr(i) for i in range(97, 123)]
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    uni_code = dict(zip(alpha, code))


    def code(letter):
        result = ""
        for key, value in uni_code.items():
            if key == letter:
                result = result + value
        return result

    def word_to_code(word):
        return "".join([code(letter) for letter in word])

    result = [word_to_code(word) for word in words]
    return len(set(result))




words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))