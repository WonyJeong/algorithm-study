#9184
import sys
input = sys.stdin.readline

'''
입력 >>
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1

출력 >>
w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1
'''


def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        dp[20][20][20] = w(20,20,20)
        return dp[20][20][20]

    elif dp[a][b][c]:
        return dp[a][b][c]
    
    elif a < b and b < c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    
    return dp[a][b][c]
 

if __name__ == '__main__':
    dp = [[[0]*21 for _ in range(21)]for _ in range(21)] # a,b,c가 20보다 크면 다 모두 20인 결과와 같으므로 배열의 크기는 20을 넘어가지 않는다.
    while True:
        a,b,c = map(int, input().strip().split())
        if a==-1 and b==-1 and c==-1:
            break
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')