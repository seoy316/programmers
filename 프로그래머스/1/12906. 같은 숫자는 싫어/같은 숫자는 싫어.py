from collections import deque

def solution(arr):
    answer = []
    stack = deque()

    for a in arr:

        if stack and stack[-1] == a:
            stack.append(a)

        else:
            stack.append(a)
            answer.append(a)

    return answer