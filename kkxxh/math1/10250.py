#10250
import sys
# H:호텔 층 , W:층의 방 수 , N:손님 번호

input = sys.stdin.readline

T = int(input())
for i in range(0,T):
    H, W, N = map(int, input().strip().split()) 
    floor = 0 #최종 층수
    room = 0 #최종 방 번호
    if N % H == 0:
        floor = H * 100
        room = N // H
    else:
        floor = (N % H) * 100
        room = 1 + N // H
    print(floor + room)

#수정 끝