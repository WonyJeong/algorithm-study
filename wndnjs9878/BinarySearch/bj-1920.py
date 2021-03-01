import sys
input = sys.stdin.readline

def solution(N, A, M, check):
    A = sorted(A)
    for ch in check :
        start = 0
        end = N-1
        answer = 0
        while (start <= end):
            mid = (start + end) // 2
            if A[mid] == ch :
                answer = 1
                break
            elif ch < A[mid] :
                end = mid - 1
            else : 
                start = mid +1
        print(answer)


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    check = list(map(int, input().strip().split()))
    solution(N, A, M, check)

