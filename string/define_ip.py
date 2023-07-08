address = "1.1.1.1"
num = []
for item in address:
    if item != '.':
        num.append(item)
    elif item == '.':
        x =item.replace('.', '[.]')
        num.append(x)
print(num)

'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''