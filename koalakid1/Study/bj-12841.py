import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    crosses = list(map(int, input().strip().split()))
    lefts = list(map(int, input().strip().split()))
    rights = list(map(int, input().strip().split()))

    distance = crosses[n-1] + sum(lefts)
    left = 0
    right = sum(rights)
    if distance >= crosses[0] + right:
        cross = 1
        distance = crosses[0] + right
        for i in range(1, n-1):
            left += lefts[i-1]
            right -= rights[i-1]
            if distance > crosses[i] + left + right:
                distance = crosses[i] + left + right
                cross = i + 1

    else:
        cross = n
        for i in range(1, n-1):
            left += lefts[i-1]
            right -= rights[i-1]
            if distance >= crosses[i] + left + right:
                distance = crosses[i] + left + right
                cross = i + 1
    print(cross, distance)
