#8958
import sys
input = sys.stdin.readline
T = int(input().strip())
for i in range(0,T) :
    quizResult = input().strip()
    # print(quizResult[1])
    cnt = 0
    score = 0
    for j in range(0, len(quizResult)) :
        if quizResult[j] == 'O' :
            cnt += 1
            score += cnt
        elif quizResult[j] == 'X' :
            cnt = 0
    print(score)