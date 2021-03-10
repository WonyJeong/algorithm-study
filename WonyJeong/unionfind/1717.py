# import sys

# input = sys.stdin.readline

# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         y = find(parent[x])
#         parent[x] = y
#         return y


# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x != y:
#         parent[y] = x


# def solution(N, M, query):
#     global parent
#     parent = [i for i in range(N + 1)]
#     for command, a, b in query:
#         if command == 0:
#             union(a, b)
#         else:
#             if find(a) == find(b):
#                 print("YES")
#             else:
#                 print("NO")
#     print(parent)


import sys

input = sys.stdin.readline


def find(u):
    if arr[u] == u:
        return u
    else:
        v = find(arr[u])
        arr[u] = v
        return v


def union(nodes):
    u, v = nodes
    u = find(u)
    v = find(v)
    if not u == v:
        arr[v] = u


def solution(N, M, query):
    global arr
    arr = [i for i in range(N + 1)]
    for q in query:
        cmd, u, v = q
        if cmd == 0:
            print(arr)
            union(sorted([u, v]))
        else:
            print("YES" if find(u) == find(v) else "NO")


if __name__ == "__main__":
    # N, M = map(int, input().strip().split())
    # query = []
    # for _ in range(M):
    #     query.append(list(map(int, input().strip().split())))
    # solution(N, M, query)
    solution(
        7,
        8,
        [
            [0, 1, 3],
            [1, 1, 7],
            [0, 7, 6],
            [1, 7, 1],
            [0, 3, 7],
            [0, 4, 2],
            [0, 1, 1],
            [1, 1, 1],
        ],
    )
