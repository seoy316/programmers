def solution(m, n, puddles):
    
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for m_, n_ in puddles:
        dp[n_][m_] = -1
    
    for n_ in range(1, n+1):
        for m_ in range(1, m+1):
            if n_ == 1 and m_== 1:
                dp[n_][m_] = 1
                continue
              
            if dp[n_][m_]== -1:
                dp[n_][m_] = 0
                continue
            
            dp[n_][m_] = (dp[n_-1][m_] + dp[n_][m_-1]) 
        
    return dp[-1][-1] % 1000000007