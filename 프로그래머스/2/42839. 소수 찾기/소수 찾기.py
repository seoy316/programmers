from itertools import *


def sieve_of_eratosthenes(num):

    arr = [True for i in range(num + 1)]

    for i in range(2, int(num ** (1 / 2)) + 1):
        if arr[i]:
            j = 2
            while i * j <= num:
                arr[i * j] = False
                j += 1

    return arr


def solution(numbers):
    answer = 0

    num = list(numbers)
    result = []

    for i in range(1, len(num)+1):
        for j in list(permutations(num, i)):
            n = int(''.join(j))
            if n > 1:
                result.append(n)

    result = list(set(result))
    result.sort()

    n = sieve_of_eratosthenes(result[-1])

    for i in result:
        if n[i]:
            answer+=1

    return answer