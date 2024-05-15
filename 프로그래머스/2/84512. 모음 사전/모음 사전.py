from itertools import *

def solution(word):

    words = ['A', 'E', 'I', 'O', 'U']
    result = []

    for i in range(1, len(words)+1):
        for j in list(product(words, repeat=i)):
            result.append(''.join(j))

    result.sort()


    return result.index(word) + 1
