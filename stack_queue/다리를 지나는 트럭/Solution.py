import queue
def solution(bridge_length, weight, truck_weights):
    q = queue.Queue()   #큐 생성
    time = 1    #시간
    total = 0   # 다리 위에 올라가 있는 트럭의 총 무게
    total_truck = len(truck_weights) # 총 트럭의 개수
    idx = 0 # 트럭 리스트의 인덱스
    for i in range(bridge_length-1): q.put(0)
    while not q.empty():
        if idx != total_truck:
            if weight >= total + truck_weights[idx]:
                total += truck_weights[idx]
                q.put(truck_weights[idx])
                idx +=1
                print(idx)
            else :
                q.put(0)
        total -= q.get()
        time += 1
    
    return time