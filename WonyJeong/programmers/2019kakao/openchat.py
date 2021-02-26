import sys

input = sys.stdin.readline


def solution(record):
    answer = []
    dic = {}
    for rec in record:
        temp = rec.split(" ")
        uuid = temp[1]
        if temp[0] == "Enter":
            if not uuid in dic.keys():
                dic[uuid] = set()
            dic[uuid] = temp[2]
            answer.append([0, uuid])
        elif temp[0] == "Leave":
            answer.append([1, uuid])
        else:
            if not uuid in dic.keys():
                dic[uuid] = set()
            dic[uuid] = temp[2]

    result = []
    for command, uuid in answer:
        if command == 0:
            result.append(dic[uuid] + "님이 들어왔습니다.")
        else:
            result.append(dic[uuid] + "님이 나갔습니다.")

    return result


if __name__ == "__main__":
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
