import sys
from itertools import permutations

input = sys.stdin.readline


def setPrime():
    len_ = 10000000
    arr = [False for _ in range(len_)]
    arr[0] = True
    arr[1] = True
    for i in range(2, len_):
        if arr[i] == False:
            for j in range(i * 2, len_, i):
                arr[j] = True
    return arr


def solution(numbers):
    answer = 0
    prime = setPrime()
    numbers = list(map(str, numbers))

    for i in range(1, len(numbers) + 1):
        for per in permutations(numbers, i):
            idx = int("".join(per))
            if prime[idx] == False:
                answer += 1
                prime[idx] = True

    return answer


if __name__ == "__main__":
    print(solution("17"))
