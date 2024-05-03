def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for h, t in zip(phone_book, phone_book[1:]):
        if t.startswith(h):
            return False
    return True