#2170
import sys
input = sys.stdin.readline

'''
4
3 5
1 3
6 7
2 5
'''

def solution(N,line):
    answer = 0
    
    #[left, right] : 현재 합치고 있는 구간
    left = -sys.maxsize
    right = -sys.maxsize

    line = sorted(line, key= lambda x: x[0])

    for i in range(N):
        if right < line[i][0] :
            answer += right - left
            left = line[i][0]
            right = line[i][1]

        else :
            right = max(right, line[i][1])

    answer += right - left
    return answer

if __name__ == '__main__':
    N = int(input().strip())
    line = []
    for _ in range(N):
        line.append(list(map(int, input().strip().split())))

    print(solution(N,line))
