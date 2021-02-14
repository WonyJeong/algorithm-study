# def solution(n):
#     answer = ""
#     arr = ["4", "1", "2"]
#     while n:
#         answer = arr[n % 3] + answer
#         n = n // 3 - (n % 3 == 0)
#     return answer


# for i in range(1, 15):
#     print(i, " : ", solution(i))

# 9494
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().strip())
    while N != 0:
        text = []
        for _ in range(N):
            text.append(len(input().strip().split()[0]))
        print(text)
        print(max(text) + 1)
        N = int(input().strip())