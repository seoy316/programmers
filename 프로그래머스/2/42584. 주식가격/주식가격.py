from collections import deque

def solution(prices):
    answer = []
    
    q = deque(prices)

    while q:
        tmp = 0
        cur = q.popleft()
        for nxt in q:
            tmp += 1
            if cur > nxt:
                break
        answer.append(tmp)

    return answer
