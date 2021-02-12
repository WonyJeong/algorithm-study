def solution(n, lost, reserve):
    answer = 0
    arr = [1 for _ in range(n + 2)]

    for l in lost:
        arr[l] = 0
    print(arr[1 : n + 1])
    for i in range(1, n + 1):
        if i in reserve:
            if arr[i] == 0:
                arr[i] = 1
                continue

            if arr[i - 1] == 0:
                arr[i - 1] = 1
                continue

            if arr[i + 1] == 0:
                arr[i + 1] = 1
                continue

    return sum(arr) - 2


print(solution(8, [5, 6], [4, 5]))
