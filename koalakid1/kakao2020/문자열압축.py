def solution(s):
    answer = 1000
    lens = len(s)
    if lens == 1:
        return 1
    for i in range(1, lens//2+1):
        other = ""
        index = 0
        checker = ""
        count = 1
        while True:
            if index + i < lens:
                if checker == s[index:index+i]:
                    count += 1
                else:
                    if count == 1:
                        other += checker
                    else:
                        other += str(count) + checker
                    checker = s[index:index+i]
                    count = 1
                index += i
            else:
                if checker == s[index:lens]:
                    count += 1
                    other += str(count) + checker
                else:
                    if count == 1:
                        other += checker
                    else:
                        other += str(count) + checker
                    other += s[index:lens]
                break
        answer = min(len(other), answer)
    return answer