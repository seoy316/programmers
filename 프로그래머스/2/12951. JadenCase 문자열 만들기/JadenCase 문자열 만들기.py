def solution(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        if len(word) > 0:
            capitalized_word = word[0].upper() + word[1:].lower()
        else:
            capitalized_word = word
        result.append(capitalized_word)
    
    return ' '.join(result)