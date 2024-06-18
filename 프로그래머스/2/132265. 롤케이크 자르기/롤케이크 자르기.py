from collections import defaultdict

def solution(topping):
    answer = 0

    topping_cnt = defaultdict(int)
    for t in topping:
        topping_cnt[t] += 1

    left = set()
    right = set(topping)

    for t in topping:
        left.add(t)
        topping_cnt[t] -= 1
        if topping_cnt[t] == 0:
            right.remove(t)
        
        if len(left) == len(right):
            answer += 1

    return answer
