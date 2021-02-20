import sys
input = sys.stdin.readline

# def solution(N, sequence):
#     count = []
#     for i in range(1,sequence[1]-sequence[0]+1):
#         for j in range(1,sequence[1]):
#             # print(i, j, sequence[0]*i+j, sequence[1]*i+j)
#             if sequence[0] * i + j == sequence[1] and sequence[1] * i + j == sequence[2]:
#                 count.append([i,j])
#                 # print(i, j)
#                 # print("log check")        
#     if len(count) > 1 :
#         return 'A'
#     elif len(count) == 1 :
#         # print(sequence[-1], i, j)
#         return sequence[-1] * count[0][0] + count[0][1]
#     else :
#         return 'B'

def solution(N, sequence):
    if N == 1:
        return 'A'
    elif N == 2 :
        if sequence[1] == sequence[0]:
            return sequence[0]
        else :
            return 'A' #무수히 많은 경우의 수 존재
    else :
        a = 0
        x = sequence[1] - sequence[0]
        y = sequence[2] - sequence[1]

        if x != 0 :
            a = y // x
        b = sequence[1] - a * sequence[0]

        for i in range(1,N):
            if sequence[i] != sequence[i-1]*a+b:
                return 'B'
        return (sequence[-1] * a + b)

if __name__ == '__main__':
    N = int(input().strip())
    sequence = list(map(int, input().strip().split()))
    print(solution(N, sequence))