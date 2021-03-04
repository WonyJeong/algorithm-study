#17298
import sys
input = sys.stdin.readline

def solution(N,A):
    answer = [-1 for _ in range(N)]
    stack = []

    for i in range(N):
        while stack and A[stack[-1]] < A[i]:
            answer[stack.pop()] = A[i]
        stack.append(i)

    return answer

if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    for element in solution(N,A):
        print(element, end=' ')