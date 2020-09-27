'''
Given a string of characters, I want the function findMiddle()/find_middle() to return the middle number in the product of each digit in the string.

Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.

Not all strings will contain digits. In this case and the case for any non-strings, return -1.

If the product has an even number of digits, return the middle two digits

Example: 1563 -> 56

NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1

'''

import re

def find_middle(string):
    if type(string) == str and re.search(r'\d',string) !=None:
        digitals=re.findall(r'\d', string)
        numbers= list(map(int,digitals))
        product =1
        for num in numbers:
            product *= num
        middle = str(product)
        if len(middle)%2 !=0:
            return int(middle[len(middle)//2])
        elif len(middle)%2 ==0:
            return int(middle[len(middle)//2-1]+ middle[len(middle)//2])
    return -1
