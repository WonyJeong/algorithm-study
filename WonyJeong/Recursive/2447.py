import sys

input = sys.stdin.readline

## 퍼온코드


def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix


star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)


# 아래는 내코드 출력은 잘되나 시간초과뜸

# def drawStar(N, i, j):
#     if i % 3 == 1 and j % 3 == 1:
#         print(" ", end="")
#     else:
#         if (N // 3) == 0:
#             print("*", end="")
#         else:
#             drawStar(N // 3, i // 3, j // 3)


# if __name__ == "__main__":
#     N = int(input().strip())
#     for i in range(0, N):
#         for j in range(0, N):
#             drawStar(N, i, j)
#         print()