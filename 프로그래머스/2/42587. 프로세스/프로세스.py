from queue import PriorityQueue
from collections import deque


def solution(priorities, location):
    answer = 0

    pq = PriorityQueue(maxsize=len(priorities))
    dq = deque()

    for idx, p in enumerate(priorities):
        pq.put(-p)
        dq.append((-p, idx))

    cnt = 1

    while pq:
        m = pq.get()

        while True:
            d = dq.popleft()

            if d[0] == m and d[1] != location:
                cnt += 1
                break
            else:
                dq.append(d)

            if d[0] == m and d[1] == location:
                answer = cnt
                return answer

    answer = cnt
    return answer
