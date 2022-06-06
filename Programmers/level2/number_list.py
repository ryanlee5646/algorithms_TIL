# level2 전화번호 목록


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            target = phone_book[i + 1]
            length = len(phone_book[i])
            if phone_book[i] == target[:length]:
                return False
    return True
