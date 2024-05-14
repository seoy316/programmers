result = 0


def dfs(graph, visited, n):
    global result

    visited[n] = True
    result += 1

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, visited, i)


def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n + 1)]
    visited = [False]*(n+1)
    global result

    for wire in wires:
        f, s = wire
        graph[f].append(s)
        graph[s].append(f)

    for wire in wires:
        f, s = wire
        graph[f].remove(s)
        graph[s].remove(f)

        dfs(graph, visited, 1)

        a = result
        b = abs(n-result)

        answer = min(abs(a-b), answer)
        visited = [False]*(n+1)
        result = 0
        graph[f].append(s)
        graph[s].append(f)


    return answer
