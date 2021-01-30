import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split())

time = (M * 60 + N - 45) % 1440
print(f'{time//60} {time%60}')