import sys
INF = sys.maxsize
input = sys.stdin.readline

def solution(s):
    answer = INF
    result = ""
    
    if len(s) == 1:
        return 1

    for i in range(1,len(s)//2+1):
        count = 1
        unit = s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i] == unit:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + unit
                unit = s[j:j+i]
                count = 1
        
        if count == 1:
            count = ""
        result += str(count) + unit
        answer = min(answer, len(result))
        result = ''

    return answer

if __name__ == '__main__':
    s = "abcabcabcabcdededededede"
    print(solution(s))