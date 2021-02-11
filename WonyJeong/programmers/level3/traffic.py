import sys
from collections import deque

input = sys.stdin.readline


def solution(lines):
    newLine = []
    cursor = []
    answer = 0
    for line in lines:
        temp = line.split("2016-09-15 ")[1].split(" ")
        end_ = temp[0].split(":")
        t = float(temp[1].split("s")[0])
        hh, mm, ss = temp[0].split(":")

        e = round(3600 * float(hh) + 60 * float(mm) + float(ss), 3)
        s = round(e - t + 0.001, 3)
        newLine.append([round(s, 3), round(e, 3)])
        cursor.append(s)
        cursor.append(e)

    newLine = sorted(newLine, key=lambda x: (x[0], x[1]))
    cursor = sorted(cursor)

    for i in cursor:
        if i >= 0 and i <= 86400:
            s = i
            e = i + 1
            temp = 0
            for s_, e_ in newLine:
                if s <= s_ < e or s <= e_ < e or (s_ < s and e < e_):
                    temp += 1
            if answer < temp:
                answer = temp
    return answer


if __name__ == "__main__":
    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s",
    ]

    lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    lines = ["2016-09-15 00:00:00.000 3s"]
    print(solution(lines))
