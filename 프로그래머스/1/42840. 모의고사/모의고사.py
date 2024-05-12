def solution(answers):
    answer = []
    
    students = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5], 
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    ls = []
    length = len(answers)
    for n, student in enumerate(students):
        tmp = 0
        while len(student) < length:
            student += student
            
        for s, a in zip(student, answers):
            if s==a:
                tmp +=1
        ls.append([n+1, tmp])
    ls.sort(key=lambda x:(x[1]), reverse=True)
    
    max_ = ls[0][1]
    
    if max_ == 0:
        return []

    for n, tmp in ls:
        if tmp-max_ >= 0:
            answer.append(n)
            
    return answer