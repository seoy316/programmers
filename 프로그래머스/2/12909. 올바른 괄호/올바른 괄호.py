def solution(s):
    answer = True
    
    stack = list()
    
    for b in s:
        if b=="(":
            stack.append(b)
        
        else:
            if not stack:
                return False
            
            else:
                stack.pop()
                
    return len(stack)==0