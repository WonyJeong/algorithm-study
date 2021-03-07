import sys


def solution(n, t, m, timetable):
    answer = ""
    tt = []
    for time in timetable:
        temp = time.split(":")
        tt.append(int(temp[0]) * 60 + int(temp[1]))
    tt = sorted(tt)

    cursor = 0

    bustable = []
    for i in range(n):
        now = 540 + i * t
        bus = [now, []]
        if cursor < len(tt):
            while len(bus[1]) < m and cursor < len(tt):
                if tt[cursor] <= now:
                    bus[1].append(tt[cursor])
                    cursor += 1
                else:
                    break
        bustable.append(bus)

    lastTime = bustable[n - 1][0]
    lastPeople = bustable[n - 1][1]

    if len(lastPeople) == 0:
        answer = lastTime
    else:
        lastPerson = lastPeople[len(lastPeople) - 1]
        if len(lastPeople) < m:
            if lastPerson <= lastTime:
                answer = lastTime
            else:
                answer = lastPerson
        else:
            answer = lastPerson - 1

    hh = "0" + str(answer // 60) if answer // 60 < 10 else str(answer // 60)
    mm = "0" + str(answer % 60) if answer % 60 < 10 else str(answer % 60)
    return hh + ":" + mm
    # print(bustable)


if __name__ == "__main__":
    print("1 : ", solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print("2 : ", solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print("3 : ", solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print("4 : ", solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print("5 : ", solution(1, 1, 1, ["23:59"]))
    print(
        "6 : ",
        solution(
            10,
            60,
            45,
            [
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
            ],
        ),
    )