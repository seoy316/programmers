def solution(triangle):
    answer = 0
    
    dp = [ [0] * (len(triangle)) for _ in range(len(triangle))]
    
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(len(triangle[i])):
            if i == len(triangle)-1:
                dp[i][j] = triangle[i][j]
                continue
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    return dp[0][0]