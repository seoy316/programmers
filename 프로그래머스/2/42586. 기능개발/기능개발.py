from collections import deque

def solution(progresses, speeds):
    ls = deque()
    answer = []

    for p, s in zip(progresses, speeds):
        ls.append(((100 - p) + s - 1) // s)

    while ls:
        tmp = 1
        work = ls.popleft()
        while ls and work >= ls[0]:
            ls.popleft()
            tmp += 1
        answer.append(tmp)
    return answer
