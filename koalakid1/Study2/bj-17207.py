from collections import deque
from bisect import bisect_left
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a = [list(map(int, input().strip().split())) for _ in range(5)]
    b = [list(map(int, input().strip().split())) for _ in range(5)]
    b = list(zip(*b))
    print(b)
    min = sys.maxsize
    index = 0
    for i in range(5):
        count = 0
        for j in range(5):
            for A, B in zip(a[i], list(b[j])):
                count += A * B

        if count <= min:
            min = count
            index = i

    Name = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
    print(Name[index])
