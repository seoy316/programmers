from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    
    sorted_count = sorted(count.values(), reverse=True)
    
    selected_count = 0
    varieties = 0
    
    for c in sorted_count:
        selected_count += c
        varieties += 1
        if selected_count >= k:
            break
    
    return varieties