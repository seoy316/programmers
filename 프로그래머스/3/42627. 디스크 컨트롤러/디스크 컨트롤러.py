import heapq
from collections import deque

def solution(jobs):
    heap = []
    jobs = deque(sorted(jobs))

    sum = 0
    last = 0
    length = len(jobs)

    while jobs or heap:
        while jobs and jobs[0][0] <= last:
            job = jobs.popleft()   
            heapq.heappush(heap, [job[1], job[0]]) 
            
        if heap:    
            time, start = heapq.heappop(heap)
            last += time   
            sum += last - start
            
        else:
            last = jobs[0][0]
        
    return sum // length