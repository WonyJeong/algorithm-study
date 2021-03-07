#1932
import sys
input = sys.stdin.readline

def solution(n,triangle):    
    '''
    index 삼각형
            0
          0   1
        0   1   2
      0   1   2   3
    0   1   2   3   4 

    값 
    7
    3 8
    8 1 0
    2 7 4 4
    4 5 2 6 5


    7
    10 15
    18 (11,16) 15
    2 7 4 4
    4 5 2 6 5
    '''
    for i in range(1,n):
        for j in range(len(triangle[i])):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == i :
                triangle[i][j] += triangle[i-1][j-1]
            else :
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[n-1])


if __name__ == '__main__':
    n = int(input().strip())
    triangle = []
    for i in range(n):
        triangle.append(list(map(int, input().strip().split())))

    print(solution(n,triangle))