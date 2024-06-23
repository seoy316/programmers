from collections import Counter

def rec(arr, n):
    result = []
    def backtrack(start, path):
        if len(path) == n:
            result.append("".join(path))
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

def solution(orders, course):
    answer = []
    
    for c in course:
        comb_counter = Counter()
        for order in orders:
            sorted_order = sorted(order)
            combinations = rec(sorted_order, c)
            comb_counter.update(combinations)
        
        if comb_counter:
            max_count = max(comb_counter.values())
            if max_count >= 2:
                for comb, count in comb_counter.items():
                    if count == max_count:
                        answer.append(comb)
    
    return sorted(answer)
