def solution(S):
    stack = []
    
    for char in S:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0

