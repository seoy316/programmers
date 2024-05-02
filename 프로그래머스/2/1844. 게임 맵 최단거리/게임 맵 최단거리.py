from collections import deque

        
#bfs

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])

    visited = [[False for j in range(m)] for i in range(n)]
    
    q = deque()
    q.append((0,0))
    
    visited[0][0] = True
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    while q:
        y, x = q.popleft() 
        for next in range(4):
            nx = x + dx[next] 
            ny = y + dy[next]
        
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx]:
                if not visited[ny][nx]: 
                    visited[ny][nx] = True
                    q.append([ny,nx])
                    
                    maps[ny][nx] = maps[y][x] +1
                    
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]