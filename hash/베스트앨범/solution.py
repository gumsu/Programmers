
from collections import defaultdict

def solution(genres, plays):
    dic, total = defaultdict(list), defaultdict(int)
    answer = []

    for i, (j, k) in enumerate(zip(genres, plays)):
        dic[j].append((k, i))
        dic[j].sort(key = lambda x: (x[0], -x[1]))
        total[j] += k
        # print(i, j, k)
    total = sorted(total.items(), key = lambda x: -x[1])

    for genre, play in total:
        cnt = 0
        while cnt < 2 and dic[genre]:
            a, b = dic[genre].pop()
            answer.append(b)
            cnt += 1
    # print(dic)
    # print(total)

    return answer