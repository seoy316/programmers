def quick_sort(arr, pivot):
    right = 0
    for x in arr:
        if x >= pivot:
            right += 1

    return right


def solution(citations):
    answer = 0

    citations.sort()
    length = len(citations)

    for h in range(1, length + 1):
        max_ = quick_sort(citations, h)

        if h <= max_:
            answer = max(answer, h)

        if max_ < h:
            break

    return answer