def solution(n, words):
    used_words = set()
    previous_word = words[0][0]
    
    for i, word in enumerate(words):
        if word in used_words or word[0] != previous_word[-1]:
            player_number = (i % n) + 1
            turn_number = (i // n) + 1
            return [player_number, turn_number]
        
        used_words.add(word)
        previous_word = word

    return [0, 0]
