import math
def solution(n):
    answer = ''
    m = int(math.log((n * 2) / 3 + 1, 3))
    n -= 3  * (3 ** m - 1) // 2
    if n == 0:
        answer = "4" * m
    else:
        for i in range(m,0,-1):
            r = n // (3 ** i)
            n %= 3 ** i
            if n == 0:
                answer += str(2 ** ((r-1)%3))
            else:
                answer += str(2 ** r)
        answer += str(2 ** ((n-1) % 3))

    return answer

print(solution(1))