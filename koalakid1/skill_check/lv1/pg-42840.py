def solution(answers):
    list2 = [1, 3, 4, 5]
    list3 = [3, 1, 2, 4, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    for index, answer in enumerate(answers):
        if answer == index % 5 + 1:
            count1 += 1
        if (answer == 2 and index % 2 == 0) or (answer == list2[index // 2 % 4] and index % 2 == 1):
            count2 += 1
        if answer == list3[index // 2 % 5]:
            count3 += 1
    answer = []
    m = max(count1, count2, count3)
    if m == count1:
        answer.append(1)
    if m == count2:
        answer.append(2)
    if m == count3:
        answer.append(3)

    return answer
