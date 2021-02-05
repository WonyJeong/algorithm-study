import sys

input = sys.stdin.readline


def findSubsequence(N, S, arr):
    stack = [arr[0], 0]
    for i in range(1, len(arr)):
        temp = []
        while stack:
            top = stack.pop()
            if top > S and arr[i] > 0:
                continue
            temp.append(top)
            temp.append(arr[i] + top)
        stack = temp

    answer = len(list(filter(lambda x: stack[x] == S, range(len(stack)))))
    print(answer - 1 if S == 0 else answer)


if __name__ == "__main__":
    N, S = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    findSubsequence(N, S, sorted(arr))
