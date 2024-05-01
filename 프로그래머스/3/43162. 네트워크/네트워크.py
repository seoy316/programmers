def dfs(graph, v, visited, n):
    
    visited[v] = True
    
    for neighbor in range(n):
        if not visited[neighbor] and graph[v][neighbor]:
            dfs(graph, neighbor, visited, n)


def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for v in range(n):
        if not visited[v]:
            dfs(computers, v, visited, n)
            answer +=1
    return answer