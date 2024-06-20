from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = deque(maxlen=cacheSize)
    total_time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            total_time += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            total_time += 5
            
    return total_time

