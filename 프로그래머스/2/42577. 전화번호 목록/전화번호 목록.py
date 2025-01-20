from collections import Counter
def solution(phone_book):
    phone_hash = {phone: True for phone in phone_book}
    # print(phone_hash)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_hash:
                return False
    return True