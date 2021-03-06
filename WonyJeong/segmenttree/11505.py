import sys

input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = (
            init(node * 2, start, (start + end) // 2)
            * init(node * 2 + 1, (start + end) // 2 + 1, end)
            % 1000000007
        )
        return tree[node] % 1000000007


def subMul(node, start, end, left, right):
    if left > end or right < start:
        return 1
    else:
        if left <= start and right >= end:
            return tree[node] % 1000000007
        else:
            return (
                subMul(node * 2, start, (start + end) // 2, left, right)
                * subMul(node * 2 + 1, (start + end) // 2 + 1, end, left, right)
                % 1000000007
            )


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    if tree[node] == 0:
        tree[node] = diff
    else:
        tree[node] = int(tree[node] * diff) % 1000000007

    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)


if __name__ == "__main__":
    n, m, k = map(int, input().strip().split())
    tree = [0] * 3000000
    l = []
    for _ in range(n):
        l.append(int(input().strip()))

    init(1, 0, n - 1)
    for _ in range(m + k):
        a, b, c = map(int, input().strip().split())
        if a == 1:
            b = b - 1
            if l[b] == 0:
                diff = c
            elif c == 0:
                diff = c
            else:
                diff = c / l[b]
            l[b] = c
            update(1, 0, n - 1, b, diff)
        elif a == 2:
            print(subMul(1, 0, n - 1, b - 1, c - 1))
