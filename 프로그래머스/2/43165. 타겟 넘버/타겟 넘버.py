def solution(numbers, target):
    answer = 0
    def dfs(tmp, length):
        nonlocal answer
        
        if length == len(numbers):
            if tmp == target:
                answer += 1
                return
            return
        
        if length == 1:
            for sign in [-1, 1]:
                dfs(sign*numbers[0]+numbers[length], length+1)
                dfs(sign*numbers[0]-numbers[length], length+1)
                
        else:
            dfs(tmp+numbers[length], length+1)
            dfs(tmp-numbers[length], length+1)               

    
    dfs(numbers[0], 1)    
    
    return answer