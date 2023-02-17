'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''

def reverse():
    given_int = int(input())
    str_int = str(given_int)
    arr = list(str_int.strip(''))
    arr.reverse()
    for j in range(len(arr)):
        if arr[j] == 0:
            arr.pop(i)
        else:
            break
    if arr[len(arr)-1] == '-':
        m = arr.pop()
        arr.insert(0, m)
        design = int(''.join(arr))
    else:
        design = int(''.join(arr))
    
    if design > ((2**31)-1) or design < (-(2**31)):
        return 0
    else:
        return design
     
grain = reverse()

print(grain)