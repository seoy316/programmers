import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    current_lcm = arr[0]
    for num in arr[1:]:
        current_lcm = lcm(current_lcm, num)
    return current_lcm
