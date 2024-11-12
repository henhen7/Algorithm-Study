from collections import deque

def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = deque()
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        # 최신화
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
            
    return answer