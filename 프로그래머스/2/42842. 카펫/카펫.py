def solution(brown, yellow):
    answer = []
 
    for h in range(1, int(yellow**(1/2))+1):
        if yellow % h == 0:
            w = yellow // h
        
            if (w+2)*(h+2) - (w*h) == brown:
                answer = [w+2, h+2]
                break
    
    return answer