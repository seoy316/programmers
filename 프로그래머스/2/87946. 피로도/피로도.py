answer = 0


def dfs(k, cnt, dungeons, visited):
    global answer

    for i in range(len(dungeons)):
        answer = max(answer, cnt)
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False
            
    if len(dungeons) == answer:
        return


def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]
    dfs(k, 0, dungeons, visited)

    return answer
