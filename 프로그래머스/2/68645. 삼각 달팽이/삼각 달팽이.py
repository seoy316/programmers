def solution(n):
    triangle = [[0] * i for i in range(1, n + 1)]
    
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # down
                x += 1
            elif i % 3 == 1:  # right
                y += 1
            else:  # up
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    
    answer = []
    for row in triangle:
        answer.extend(row)
    
    return answer