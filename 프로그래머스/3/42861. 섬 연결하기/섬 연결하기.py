parent = []


def find(x):
    global parent

    if parent[x] != x:
        return find(parent[x])

    return x


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    global parent

    parent = [x for x in range(n)]
    costs.sort(key=lambda x: x[2])

    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
            
    print(parent)

    return answer