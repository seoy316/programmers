def solution(clothes):
    answer = 1
    cloth = {}
    for _, kind in clothes:
        if kind not in cloth:
            cloth[kind] = 1
        else:
            cloth[kind] += 1

    for v in cloth.values():
        answer *= (v+1)
    return answer-1