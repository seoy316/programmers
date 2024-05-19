def solution(board, moves):
    answer = 0
    bucket = []
    board = [list(x) for x in zip(*board)]
    
    for i in board:
        while 0 in i:
            i.remove(0)
       
    for move in moves:
        length = len(board[move-1])

        if length == 0:
            continue
        
        bucket.append(board[move-1].pop(0))

        if len(bucket) >= 2 and bucket[-1:] == bucket[-2:-1]:
            bucket.pop()
            bucket.pop()
            answer += 2
    
    return answer