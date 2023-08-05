'''
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
'''

def squareIsWhite(coordinates: str) -> bool:
    num = []
    strs = []
    for i in coordinates:
        if i.isdigit():
            num.append(i)
        else:
            strs.append(i)
    x = dict(zip(strs, num))
    for key, value in x.items():
        if key == 'a' or key == 'c'  or key == 'e' or key == 'g':
            if int(value) % 2 != 0:
                return False
            else:
                return True
        elif key == 'b' or key == 'd' or key == 'f' or key == 'h':
            if int(value) % 2 == 0:
                return False
            else:
                return True
            
coordinates = "a1"
print(squareIsWhite(coordinates))