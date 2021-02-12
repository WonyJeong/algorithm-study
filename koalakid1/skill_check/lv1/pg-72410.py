def solution(id):
    id = id.upper()
    answer = ""
    for i in id:
        if i.isalnum() or i in "-_.":
            answer += i

    while ".." in answer:
        answer = answer.replace("..", ".")

    if len(answer) > 1 and answer[0] == ".":
        answer = answer[1:]
    if answer[-1] == ".":
        answer = answer[:-1]

    if answer == "":
        answer = "aaa"

    if len(answer) >= 16:
        if answer[15] == ".":
            answer = answer[:15]
        else:
            answer = answer[:16]
    elif len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))

    return answer.lower()
