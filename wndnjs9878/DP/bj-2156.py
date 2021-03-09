#2156
import sys
input = sys.stdin.readline

'''
6
6
10
13
9
8
1
'''

def solution(N, podo):
    answer = [0 for _ in range(N)]  #각 포도주 번호를 마실 때까지 마신 최대 양을 저장

    if N == 1:
        return podo[0]
    if N == 2 :
        return podo[0] + podo[1]
    answer[0] = podo[0]
    answer[1] = podo[0] + podo[1]
    answer[2] = max(podo[0]+podo[1], podo[0] + podo[2], podo[1] + podo[2])

    for i in range(3, N):
        answer[i] = max(answer[i-1], podo[i] + podo[i-1] + answer[i-3], podo[i] + answer[i-2])

    return answer[-1]

if __name__ == '__main__':
    N = int(input().strip())
    podo = []
    for _ in range(N):
        podo.append(int(input().strip()))
    print(solution(N, podo))
    