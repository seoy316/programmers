def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x:x[0])
    start = routes[0][0]
    end = routes[0][1]
    
    for i in range(1, len(routes)):
        if start <= routes[i][0] <= end:
            start = max(start, routes[i][0])
            end = min(end, routes[i][1])
        else:
            end = max(end, routes[i][1])
            answer+=1
                
    return answer+1