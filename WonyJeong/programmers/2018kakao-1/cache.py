import sys
from collections import deque

input = sys.stdin.readline


def solution(cacheSize, cities):
    answer = 0
    q = deque([])

    for city in cities:
        city = city.lower()

        if cacheSize > 0:
            if len(q) < cacheSize:
                if not city in q:
                    q.append(city)
                    answer += 5
                else:
                    q.remove(city)
                    q.append(city)
                    answer += 1
            else:
                if not city in q:
                    q.popleft()
                    q.append(city)
                    answer += 5
                else:
                    q.remove(city)
                    q.append(city)
                    answer += 1
        else:
            answer += 5

    return answer


if __name__ == "__main__":
    print(
        solution(
            3,
            [
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
                "Jeju",
                "Pangyo",
                "Seoul",
                "NewYork",
                "LA",
            ],
        )
    )
