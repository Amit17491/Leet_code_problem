'''2011. Final Value of Variable After Performing Operations
Easy
1.3K
156
Companies
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

 

Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
'''

from typing import List
def finalValueAfterOperations(operations: List[str]) -> int:
        num = []
        for item in operations:
            if item == 'X--' or item == '--X':
                num.append(-1)
            else:
                num.append(1)
        return sum(num)

operations = ["--X","X++","X++"]
print(finalValueAfterOperations(operations))