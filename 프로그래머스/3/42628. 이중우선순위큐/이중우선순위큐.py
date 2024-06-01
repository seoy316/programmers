import heapq

def solution(operations):
    answer = []
    
    heap = []
    
    for o in operations:
        c, n = o.split(" ")
        
        if c=="I":
            heapq.heappush(heap, int(n))
            
        elif c=="D" and heap:
            if n == "1":
                x = heapq.nlargest(n=1, iterable=heap)
                heap.remove(x[0])
                    
            elif n == "-1":
                heapq.heappop(heap)
    

    if not heap:
        answer = [0, 0]
    else:
        x = heapq.nlargest(n=1, iterable=heap)
        answer = [x[-1], heap[0]]
    
    return answer