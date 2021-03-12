import sys

input = sys.stdin.readline


def solution(N, arr):
    answer = 0
    temp = []

    for i in range(1, N):
        if arr[i - 1] > arr[i]:
            if len(temp) == 0:
                temp.append(i)
            else:
                return 0

    if len(temp) == 0 or len(arr) == 2:
        return N
    else:
        idx = temp[0]
        if 1 < idx < N - 1:
            a, b, c, d = arr[idx - 2], arr[idx - 1], arr[idx], arr[idx + 1]
            if a <= c:
                answer += 1
            if b <= d:
                answer += 1
            return answer

        elif idx == 1:
            a, b, c = arr[idx - 1], arr[idx], arr[idx + 1]
            if a <= c:
                return 2
            else:
                return 1
        else:
            a, b, c = arr[idx - 2], arr[idx - 1], arr[idx]
            if a <= c:
                return 2
            else:
                return 1

    return answer


if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(solution(N, arr))
