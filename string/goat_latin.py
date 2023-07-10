'''
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.

 

Example 1:

Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
'''

def toGoatLatin(sentence: str) -> str:
        sentence = sentence.split(' ')
        words = ""
        for i in range(len(sentence)):
            if sentence[i][0].lower() == 'a' or sentence[i][0].lower() == 'e' or sentence[i][0].lower() == 'i' or sentence[i][0].lower() == 'o' or sentence[i][0].lower() == 'u':
               words = words + sentence[i] + 'maa' + i*'a' + " "
            else:
                words = words + sentence[i][1:] + sentence[i][0] + 'maa' + i*'a' +  " "
        return words.strip()

sentence = "I speak Goat Latin"
print(toGoatLatin(sentence))
