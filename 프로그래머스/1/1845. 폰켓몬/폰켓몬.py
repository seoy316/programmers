def solution(nums):
    answer = 0
    
    cnt = len(nums)
    
    pick = cnt//2
    pon = dict()
    for n in nums:
        if n in pon:
            pon[n] += 1
        else:
            pon[n] = 1
            
    if pick > len(pon):
        answer = len(pon)
    else:
        answer = pick

    return answer