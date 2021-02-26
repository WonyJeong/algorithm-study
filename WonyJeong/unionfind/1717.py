import sys

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


def solution(N, M, query):
    global parent
    parent = [i for i in range(N + 1)]
    for command, a, b in query:
        if command == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
    print(parent)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    query = []
    for _ in range(M):
        query.append(list(map(int, input().strip().split())))
    solution(N, M, query)
