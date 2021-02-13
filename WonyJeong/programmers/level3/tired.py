import heapq


def solution(n, works):
    answer = 0
    h = []
    for work in works:
        heapq.heappush(h, (-work, work))

    for _ in range(n):
        top = heapq.heappop(h)[1]
        if top == 0:
            return 0

        heapq.heappush(h, (-(top - 1), top - 1))

    for item in h:
        answer += item[1] ** 2

    return answer


print(solution(4, [4, 3, 3]))
