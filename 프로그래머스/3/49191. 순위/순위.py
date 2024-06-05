def solution(n, results):
    wins = [[False] * (n + 1) for _ in range(n + 1)]
    
    for winner, loser in results:
        wins[winner][loser] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if wins[i][k] and wins[k][j]:
                    wins[i][j] = True

    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if wins[i][j] or wins[j][i]:
                count += 1
        if count == n - 1:
            answer += 1

    return answer
