#10950
#첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.

import sys

input = sys.stdin.readline
N = int(input().strip())
for i in range(N) :
    a,b = map(int, input().strip().split())
    print(a+b)

