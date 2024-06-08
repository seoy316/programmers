from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort()

    route = [] 
    stack = ["ICN"]

    while stack:
        top = stack[-1]
        if not graph[top]:
            route.append(stack.pop())
        else:
            stack.append(graph[top].pop(0))
    
    return route[::-1]
