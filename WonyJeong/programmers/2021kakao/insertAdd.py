import sys

input = sys.stdin.readline


def reConvertTime(time):
    hh = "0" + str(time // 3600) if time // 3600 < 10 else str(time // 3600)
    time %= 3600
    mm = "0" + str(time // 60) if time // 60 < 10 else str(time // 60)
    time %= 60
    ss = "0" + str(time // 1) if time // 1 < 10 else str(time // 1)
    return hh + ":" + mm + ":" + ss


def convertTime(time):
    temp = time.split(":")
    return int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])


def solution(play_time, adv_time, logs):
    answer = ["", 0, 0]
    boundary = [0]
    timetable = []
    pt = convertTime(play_time)
    at = convertTime(adv_time)
    for time in logs:
        time_ = time.split("-")
        start = convertTime(time_[0])
        end = convertTime(time_[1])
        timetable.append([start, end])
        boundary.append(start)
        boundary.append(end)
    boundary = sorted(boundary)

    timetable = sorted(timetable, key=lambda x: (x[0]))

    for s in boundary:
        e = s + at if s + at <= pt else pt
        temp = 0
        cum = 0
        print("--------------------------")
        print("광고 : ", s, " ~ ", e)
        for s_, e_ in timetable:
            if s_ <= s and e <= e_:
                print("영상 : ", s_, " ~ ", e_)
                cum += e - s
                temp += 1
            elif s_ < s and s <= e_ <= e:
                print("영상 : ", s_, " ~ ", e_)
                cum += e_ - s
                temp += 1
            elif s <= s_ and e_ <= e:
                print("영상 : ", s_, " ~ ", e_)
                cum += e_ - s_
                temp += 1
            elif s < s_ < e and e <= e_:
                print("영상 : ", s_, " ~ ", e_)
                cum += e_ - s_
                temp += 1
        print("광고시청 유저 수 : ", temp)
        print("광고누적 재생시간 : ", cum)

        if answer[1] <= temp and answer[2] < cum:
            answer[0] = s
            answer[1] = temp
            answer[2] = cum

        if e == pt:
            break

    return reConvertTime(answer[0])


if __name__ == "__main__":
    print(
        solution(
            "99:59:59",
            "25:00:00",
            [
                "69:59:59-89:59:59",
                "01:00:00-21:00:00",
                "79:59:59-99:59:59",
                "11:00:00-31:00:00",
            ],
        )
    )
    # print(
    #     solution(
    #         "50:00:00",
    #         "50:00:00",
    #         ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
    #     )
    # )
