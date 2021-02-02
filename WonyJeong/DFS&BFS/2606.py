import sys

input = sys.stdin.readline


def birus(N, M, dic):
    visited = [False] * (N + 1)
    stack = [1]
    answer = -1
    while stack:
        top = stack.pop()
        if visited[top] == False:
            visited[top] = True
            answer += 1
            if top in dic.keys():
                stack += sorted(dic[top], reverse=True)
                del dic[top]
    print(answer)


if __name__ == "__main__":
    dic = {}
    N = int(input().strip())
    M = int(input().strip())
    for _ in range(0, M):
        n1, n2 = map(int, input().strip().split())
        if n1 not in dic:
            dic[n1] = set()
        if n2 not in dic:
            dic[n2] = set()
        dic[n1].add(n2)
        dic[n2].add(n1)

    birus(N, M, dic)

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7