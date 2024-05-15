import collections


def solution(n, lost, reserve):
    losts = list(collections.Counter(lost) - collections.Counter(reserve))
    reserves = list(collections.Counter(reserve) - collections.Counter(lost))
    
    answer = n - len(losts)
    
    losts.sort()
    reserves.sort()

    for l in losts:
        for r in reserves:
            if abs(l - r) == 1:
                answer += 1
                reserves.remove(r)
                break

    return answer

