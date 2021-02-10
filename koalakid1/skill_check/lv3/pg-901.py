def solution(n, k):
    answer = []
    number = [i for i in range(1, n+1)]
    factorial = 1
    for i in range(2, n+1):
        factorial *= i

    while n >= 1:
        factorial //= n
        q = k // factorial
        k %= factorial
        if k == 0:
            answer.append(number.pop(q-1))
        else:
            answer.append(number.pop(q))
        n -= 1
    return answer
