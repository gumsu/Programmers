def solution(phone_book):
    dic = dict()
    
    for i in phone_book:
        if i not in dic:
            dic[i] = 1
    for number in phone_book:
        tmp = ""
        for i in number:
            tmp += i
            if tmp in dic and tmp != number:
                return False
    return True