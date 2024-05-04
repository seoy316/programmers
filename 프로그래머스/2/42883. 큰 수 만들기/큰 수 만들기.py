from collections import deque

def solution(number, k):
    stack = []
    number= deque(number)
    
    stack.append(number.popleft()) 
    
    while number:
        n = number.popleft()
        while k > 0 and stack and stack[-1] < n:
            stack.pop()
            k-=1    
        stack.append(n)
        
    for n in number:
        stack.append(n)
    
    while k > 0:
        stack.pop()
        k-=1
        
    
    return ''.join(stack)