# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


def solution(new_id):
    answer = new_id
    # step 1
    answer = answer.lower()

    # step 2
    temp = ""
    for char in answer:
        asci = ord(char)
        if 97 <= asci <= 122 or asci == 95 or asci == 45 or asci == 46:
            temp += char
    answer = temp
    print(answer)
    # step 3
    while True:
        if not ".." in answer:
            break
        else:
            answer = answer.replace("..", ".")

    # step 4
    if len(answer) > 0:
        if answer[0] == ".":
            answer = answer.replace(".", "", 1)

    if len(answer) > 0:
        if answer[len(answer) - 1] == ".":
            answer = answer[0 : len(answer) - 1]

    # step 5
    if answer == "":
        answer += "a"

    # step 6
    if len(answer) >= 16:
        answer = answer[0:15]
        while True:
            if answer[len(answer) - 1] == ".":
                answer = answer[0 : len(answer) - 1]
            else:
                break

    # step 7
    while len(answer) < 3:
        lastChar = answer[len(answer) - 1]
        answer += lastChar

    return answer


if __name__ == "__main__":
    # print(solution("...!@BaT#*..y.abcdefghijklm"))
    # print(solution("z-+.^."))
    # print(solution("=.="))
    print(solution("123_.def"))
    # print(solution("abcdefghijklmn.p"))
