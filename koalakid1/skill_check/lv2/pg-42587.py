from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        q = queue.popleft()
        for i in queue:
            if q < i:
                queue.append(q)
                location -= 1
                location %= len(queue)
                break
        else:
            answer += 1
            if location == 0:
                return answer
            location -= 1
            location %= len(queue)
