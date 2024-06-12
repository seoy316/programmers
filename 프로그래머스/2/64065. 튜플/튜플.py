import re
from collections import defaultdict

def solution(s):
    answer = []
    
    numbers = re.findall(r'\d+', s)
    numbers = list(map(int, numbers))
    
    counter = defaultdict(int)
    for num in numbers:
        counter[num] += 1
    
    answer = sorted(counter, key=lambda x: counter[x], reverse=True)
    
    return answer
