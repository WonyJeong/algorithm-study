import math


def getCombination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def solution(n_):
    answer = 0

    n = n_
    r = 0
    while n >= r:
        answer += getCombination(n, r)
        print(f"{n} C {r} = {getCombination(n, r)}")
        n -= 1
        r += 1

    return answer


for i in range(1, 20):
    print(i, solution(i))