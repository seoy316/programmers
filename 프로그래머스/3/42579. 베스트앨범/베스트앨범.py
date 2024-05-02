import operator

def solution(genres, plays):

    idx = []
    for i in range(len(genres)):
        idx.append(i)

    dic = {}
    dic2 ={}
    d = []

    for g, p in zip(genres, plays):
        if g not in dic:
            dic[g] = p
            dic2[g] =1
        else:
            dic[g] += p
            dic2[g] +=1
        d.append([g, p])

    dic = dict(sorted(dic.items() ,key= operator.itemgetter(1), reverse=True))

    answer = {}
    for i, comb in zip(idx, d):
        if i not in answer:
            answer[i] = comb
        else:
            answer[i] = comb

    album = []
    answer = dict(sorted(answer.items(), key= operator.itemgetter(1), reverse=True))

    for i in dic.keys():
        print(i)
        cnt = 0
        for k, v in zip(answer.keys(), answer.values()):
            if i == v[0]:
                if dic2[i] < 2:
                    album.append(k)
                elif dic2[i] >= 2 and cnt < 2:
                    album.append(k)
                    cnt +=1
    return album