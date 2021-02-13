def solution(n):
    answer = ""
    arr = ["4", "1", "2"]
    while n:
        answer = arr[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
    return answer


for i in range(1, 15):
    print(i, " : ", solution(i))
