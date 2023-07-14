'''
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".

'''

from typing import List
def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
        num = {}
        for word in list1:
            if word == " ":
                return False
            if word in list2:
                ln = list1.index(word) + list2.index(word)
                num[word] = ln

        lst = []
        for i , j in num.items():
            if j == min(num.values()):
                lst.append(i)
        return lst

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1, list2))