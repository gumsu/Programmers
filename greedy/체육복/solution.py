def solution(n, lost, reserve):
    able = [1]*n
    for i in range(len(reserve)):
        able[reserve[i]-1] += 1
    for i in range(len(lost)):
        able[lost[i]-1] -= 1
    for i,a in enumerate(able):
        if a == 0:
            if i>0 and able[i-1] ==2:
                able[i] +=1
                able[i-1] -=1
            elif i<n-1 and able[i+1] ==2:
                able[i] +=1
                able[i+1] -=1
    return able.count(1)+able.count(2)