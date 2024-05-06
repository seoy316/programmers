from functools import cmp_to_key

def compare(a, b):
    num1 = int(a + b)
    num2 = int(b + a)

    if num1 > num2:
        return -1  
    elif num1 < num2:
        return 1 
    else:
        return 0

def solution(numbers):
    numbers = sorted(map(str, numbers), key=cmp_to_key(compare))
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)