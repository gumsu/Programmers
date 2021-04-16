def solution(participant, completion):
    res = dict()
    for i in participant:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    for i in completion:
        if i in res:
            res[i] -= 1
    for key, value in res.items():
        if value == 1:
            return key