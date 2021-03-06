from bisect import bisect_left

def solution(n, weak, dist):
    answer = 0
    dist = reversed(sorted(dist))
    lenw = len(weak)
    _weak = weak[:]
    for i in dist:
        start = 0
        end = 0
        count = 0
        for j in weak:
            left = bisect_left(weak,j)
            next = (j+i) % n
            right = bisect_left(weak,next) % lenw
            checker = right - left
            if right < left:
                checker += lenw
            
            if next == weak[right]:
                checker += 1
            
            print(left,right,checker)
    return answer

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])