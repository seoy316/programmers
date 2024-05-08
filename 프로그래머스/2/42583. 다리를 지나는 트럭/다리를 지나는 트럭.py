from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0 for _ in range(bridge_length)])
    truck = deque(truck_weights)

    bridge_weight = 0

    while truck or bridge:
        answer += 1
        bridge_weight -= bridge.popleft()

        if truck:
            if bridge_weight + truck[0] <= weight:
                w = truck.popleft()
                bridge_weight += w
                bridge.append(w)

            else:
                bridge.append(0)

    return answer
