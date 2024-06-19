def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            answer += 1
            
    return answer
