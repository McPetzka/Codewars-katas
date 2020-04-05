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
            return middle[len(middle)//2]
        elif len(middle)%2 ==0:
            return middle[len(middle)//2-1]+ middle[len(middle)//2]
    return -1
    

print(find_middle('s7d8jd9'))
print(find_middle('58jd9fgh/fgh6s.,sdf'))
print(find_middle(None))
print(find_middle([1,2,3]))