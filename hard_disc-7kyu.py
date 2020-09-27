'''
Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive. The files must be saved in the order they appear in the queue.

Input:
Array of file sizes (0 <= s <= 100)
Capacity of the HD (0 <= c <= 500)
Output:
Number of files that can be fully saved in the HD.
Examples:
save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, but 4+4+4+3 > 12
'''

def save(sizes, hd):
    i =0
    total =0
    while i< len(sizes) and total + sizes[i]<=hd:
        total+= sizes[i]
        i+=1
    return i
