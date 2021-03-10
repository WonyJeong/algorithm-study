import sys
input = sys.stdin.readline


'''
전깃줄이 꼬이지 않으려면
A , B 두 개의 전봇대의 위치가 각각의 전 전깃줄 위치보다 커야함.
B에서 LIS를 구하자. 그만큼만 살려두면 되자너~


입력 :
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

출력 :
3
'''


def solution(N,line):
    line = list(sorted(line.items()))
    B = []
    for key in line:
        B.append(key[1])

    # print(B)

    lis = [1] * N
    for i in range(N):
        for j in range(i):
            if B[j] < B[i] :
                lis[i] = max(lis[i], lis[j]+1)


    return N - max(lis)


if __name__ == '__main__':
    N = int(input().strip())
    line = dict()
    for i in range(N):
        A, B = map(int, input().strip().split())
        line[A] = B
    
    print(solution(N,line))
