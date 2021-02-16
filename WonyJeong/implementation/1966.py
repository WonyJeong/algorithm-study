import sys
from collections import deque

input = sys.stdin.readline


def printer(N, M, q):
    temp = [i for i in range(0, len(q))]
    dq = deque(q)
    temp = deque(temp)
    ct = 1

    while q:
        max_ = max(dq)
        bot = dq.popleft()
        bot_ = temp.popleft()
        if bot_ == M and bot == max_:
            print(ct)
            break
        if bot < max_:
            dq.append(bot)
            temp.append(bot_)
        else:
            ct += 1


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        q = list(map(int, input().strip().split()))
        printer(N, M, q)
