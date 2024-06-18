def solution(dirs):
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    
    x, y = 0, 0
    visited_paths = set()
    
    for dir in dirs:
        dx, dy = moves[dir]
        nx, ny = x + dx, y + dy
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        path = ((x, y), (nx, ny))
        reverse_path = ((nx, ny), (x, y))
        
        if path not in visited_paths:
            visited_paths.add(path)
            visited_paths.add(reverse_path)
        
        x, y = nx, ny
    
    return len(visited_paths) // 2

