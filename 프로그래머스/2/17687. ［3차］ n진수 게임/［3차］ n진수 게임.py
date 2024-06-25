def convert_to_base(num, base):
    chars = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = []
    while num > 0:
        result.append(chars[num % base])
        num //= base
    return ''.join(reversed(result))

def solution(n, t, m, p):
    required_length = t * m
    number_str = ""
    num = 0
    
    while len(number_str) < required_length:
        number_str += convert_to_base(num, n)
        num += 1
    
    result = []
    for i in range(t):
        result.append(number_str[(p - 1) + i * m])
    
    return ''.join(result)

