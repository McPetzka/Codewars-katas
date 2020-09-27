'''

Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
'''

import re

def solution(s):
   return re.sub(r"(\w)([A-Z])", r"\1 \2",s)
