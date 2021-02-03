import sys

input = sys.stdin.readline

from collections import deque


def bfs(s, e):
    history = [0 for _ in range(100001)]
    visited = [False for _ in range(100001)]
    q = deque([s])
    while q:
        bot = q.popleft()
        if bot == e:
            print(history[bot])
            break

        if visited[bot] == False:
            visited[bot] = True
            nextLocation = [bot - 1, bot + 1, bot * 2]
            for i in range(0, 3):
                if 0 <= nextLocation[i] <= 100000 and visited[nextLocation[i]] == False:
                    # 기존 his 값보다 작은 값이 탐색 되었다면 값을 바꾸어 주어야 한다.
                    if (
                        history[nextLocation[i]] == 0
                        or history[bot] + 1 < history[nextLocation[i]]
                    ):
                        history[nextLocation[i]] = history[bot] + 1
                    q.append(nextLocation[i])


if __name__ == "__main__":
    s, e = map(int, input().strip().split())
    if s < e:
        bfs(s, e)
    elif s == e:
        print(0)
    else:
        print(abs(e - s))
