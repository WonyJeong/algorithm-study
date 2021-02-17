import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input().strip())
    answer = []
    for _ in range(N):
        temp = int(input().strip())
        if temp == 0:
            answer.pop()
        else:
            answer.append(temp)
    print(sum(answer))