#9251 LCS
import sys
input = sys.stdin.readline

def solution(seq):
    answer = [[0 for _ in range(len(seq[1])+1)]  for _ in range(len(seq[0])+1)]
 

    for i in range(1,len(seq[0])+1):
      for j in range(1, len(seq[1])+1):
            if seq[0][i-1] == seq[1][j-1] :
              answer[i][j] =answer[i-1][j-1] + 1
            else :
                answer[i][j] = max(answer[i-1][j],answer[i][j-1])


    return answer[len(seq[0])][len(seq[1])]


if __name__ == '__main__':
    seq = [input().strip() for _ in range(2)]

    print(solution(seq))
