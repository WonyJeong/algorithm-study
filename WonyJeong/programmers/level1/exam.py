def scoring(arr, answers):
    temp = 0
    for i in range(0, len(answers)):
        if answers[i] == arr[i % len(arr)]:
            temp += 1
    return temp


def solution(answers):
    answer = []
    arr = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(0, 3):
        temp = arr[i]
        answer.append(scoring(arr[i], answers))

    max_ = max(answer)
    temp = []
    for i in range(len(answer)):
        if answer[i] == max_:
            temp.append(i + 1)
    return temp


print(solution([1, 2, 3, 4, 5]))
