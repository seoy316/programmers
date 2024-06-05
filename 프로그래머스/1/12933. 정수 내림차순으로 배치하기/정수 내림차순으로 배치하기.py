def solution(n):
    answer = ''
    n = sorted(str(n))
    
    for digit in reversed(n):
        answer += digit
    
    return int(answer)
