import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 

    while scoville:
        min_f = heapq.heappop(scoville)        
        if scoville and min_f < K:             
            min_s = heapq.heappop(scoville)   
            v = min_f + (min_s * 2)     
            heapq.heappush(scoville, v)        
            answer += 1                 
        elif min_f >= K :               
            heapq.heappush(scoville, min_f)    
            break                       
        else:                           
            answer = -1                 

    return answer