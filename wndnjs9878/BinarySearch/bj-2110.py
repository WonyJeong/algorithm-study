import sys
import bisect
input = sys.stdin.readline


def solved(N, C, home):
    '''
    이분탐색의 대상 : "단위거리"
    1. start : 1 (1 : 무조건 한 칸 거리로 떨어져있을수있으므로)
    2. end : 최대 단위 거리 (좌표 최대값 - 좌표 최소값)
    '''
    home = sorted(home)
    start, end = 1, max(home)-min(home)
    while True :
        mid = (start + end) // 2 
        startidx = 0
        wifi_count = 0
        while startidx < len(home):
            wifi_count +=1 
            startidx = bisect.bisect_left(home, home[startidx]+mid)
        
        if wifi_count < C:
            end = mid - 1
        else:
            start = mid + 1

        if mid == end :
            print(mid)
            break
        

if __name__ == '__main__':
    N, C = map(int, input().strip().split())
    home = [int(input().strip()) for _ in range(N)]

    solved(N,C,home)



# import sys

# input = sys.stdin.readline


# def solution(N, C, arr):
#     arr = sorted(arr)
#     start = 1
#     end = arr[N - 1] - arr[0]
#     mid = (start + end) // 2
#     result = 0

#     while start <= end:
#         mid = (start + end) // 2
#         frontHouse = arr[0]
#         count = 1

#         for i in range(1, len(arr)):
#             if arr[i] >= frontHouse + mid:
#                 count += 1
#                 frontHouse = arr[i]

#         if count >= C:
#             start = mid + 1
#             result = mid
#         else:
#             end = mid - 1

#     print(result)


# if __name__ == "__main__":
#     N, C = map(int, input().strip().split())
#     arr = []
#     for _ in range(N):
#         arr.append(int(input().strip()))
#     solution(N, C, arr)