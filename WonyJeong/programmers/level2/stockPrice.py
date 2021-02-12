def solution(prices):
    answer = [0 for _ in range(len(prices))]

    stack = [[0, prices[0], 0]]

    for i in range(1, len(prices)):
        for stock in stack:
            stock[2] += 1

        if len(stack) > 0:
            top = stack[-1]
            if top[1] <= prices[i]:
                stack.append([i, prices[i], 0])
            else:
                while stack:
                    if top[1] <= prices[i]:
                        stack.append([i, prices[i], 0])
                        break

                    popItem = stack.pop()
                    answer[popItem[0]] = popItem[2]
                    if stack == []:
                        stack.append([i, prices[i], 0])
                        break
                    top = stack[-1]
        else:
            stack.append([i, prices[i], 0])

    while stack:
        top = stack.pop()
        answer[top[0]] = top[2]

    return answer


# print(solution([1, 2, 3, 2, 3]))
print(solution([5, 4, 3, 2, 1]))
