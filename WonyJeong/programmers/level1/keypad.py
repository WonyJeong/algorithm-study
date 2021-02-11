# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #


def getDist(now, num):
    if now == "*":
        now = 10
    if now == "#":
        now = 12
    if now == 0:
        now = 11
    if num == 0:
        num = 11

    diff = abs(now - num)
    y = diff // 3
    x = diff % 3

    return x + y


def solution(numbers, hand):
    answer = ""
    l = "*"
    r = "#"
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            l = num
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            r = num
        else:
            lToNum = getDist(l, num)
            rToNum = getDist(r, num)
            if lToNum < rToNum:
                answer += "L"
                l = num
            elif lToNum > rToNum:
                answer += "R"
                r = num
            else:
                if hand == "right":
                    answer += "R"
                    r = num
                else:
                    answer += "L"
                    l = num

    return answer


if __name__ == "__main__":
    # print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
