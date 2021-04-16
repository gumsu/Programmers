def solution(participant, completion):
    n = len(participant)
    participant.sort()
    completion.sort()

    for i in range(n-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[n-1]