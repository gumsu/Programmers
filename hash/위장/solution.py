def solution(clothes):
    answer = 1
    dic = dict()
    
    for i, j in clothes:
        if j not in dic:
            dic[j] = [i]
        else:
            dic[j].append(i)
    
    # (모자 개수 + 1)*(안경 개수 + 1)*(신발 개수 + 1)
    for i in dic.values():
        answer *= len(i)+1
    return answer -1