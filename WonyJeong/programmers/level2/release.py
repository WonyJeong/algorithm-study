def solution(progresses, speeds):
    answer = []
    cursor = 0

    while cursor < len(progresses):
        print(progresses)
        if progresses[cursor] >= 100:
            temp = 0
            while cursor < len(progresses):
                if progresses[cursor] >= 100:
                    temp += 1
                    cursor += 1
                else:
                    break
            answer.append(temp)
        else:
            progresses = [i + j for i, j in zip(progresses, speeds)]

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
