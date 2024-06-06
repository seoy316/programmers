def solution(s, n):
    result = []
    
    for char in s:
        if char.islower():
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            result.append(new_char)
        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)
