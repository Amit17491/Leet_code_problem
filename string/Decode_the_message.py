'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

    Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
    Align the substitution table with the regular English alphabet.
    Each letter in message is then substituted using the table.
    Spaces ' ' are transformed to themselves.

    For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

Return the decoded message.

 

Example 1:

Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

'''

def decodeMessage(key: str, message: str) -> str:
    alphabet = [chr(i) for i in range(97, 123)]
    num = ""
    for i in key:
        if i in num or i  == " ":
            continue
        else:
            num = num + i
    x = zip(num, alphabet)
    mapping = dict(x)
    decode = ""
    for char in message:
        if char == " ":
            decode = decode + " "
        elif char in mapping:
            decode = decode + mapping[char]
        
    return decode 


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(decodeMessage(key, message))