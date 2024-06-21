import re
from collections import Counter

def multiset(s):
    s = s.lower()
    multiset = []
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if re.match(r'[a-z]{2}', pair):
            multiset.append(pair)
    return multiset

def solution(str1, str2):
    ms1 = multiset(str1)
    ms2 = multiset(str2)

    counter1 = Counter(ms1)
    counter2 = Counter(ms2)

    intersection = counter1 & counter2
    union = counter1 | counter2

    if not union:
        return 65536

    intersection_cnt = sum(intersection.values())
    union_cnt = sum(union.values())

    jaccard_similarity = intersection_cnt / union_cnt
    return int(jaccard_similarity * 65536)
