from collections import deque


def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        price = queue.popleft()

        count = 0
        for i in queue:
            count += 1
            if price > i:
                break
        answer.append(count)
    return answer
