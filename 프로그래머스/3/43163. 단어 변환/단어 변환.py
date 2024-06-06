from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words = set(words)
    queue = deque([(begin, 0)])
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == target:
            return steps
        
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != current_word[i]:
                    new_word = current_word[:i] + c + current_word[i+1:]
                    if new_word in words:
                        words.remove(new_word)
                        queue.append((new_word, steps + 1))
    
    return 0
