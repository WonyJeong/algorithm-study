#5622
import sys
input = sys.stdin.readline


def transit(word) :
    result = []
    for i in range(0, len(word)) :
        if word[i] == 'A' or word[i] == 'B' or word[i] == 'C' :
            result.append('2')
        elif word[i] == 'D' or word[i] == 'E' or word[i] == 'F' :
            result.append('3')
        elif word[i] == 'G' or word[i] == 'H' or word[i] == 'I' :
            result.append('4')
        elif word[i] == 'J' or word[i] == 'K' or word[i] == 'L' :
            result.append('5')
        elif word[i] == 'M' or word[i] == 'N' or word[i] == 'O' :
            result.append('6')
        elif word[i] == 'P' or word[i] == 'Q' or word[i] == 'R' or word[i] == 'S' :
            result.append('7')
        elif word[i] == 'T' or word[i] == 'U' or word[i] == 'V' :
            result.append('8')
        elif word[i] == 'W' or word[i] == 'X' or word[i] == 'Y' or word[i] == 'Z' :
            result.append('9')
    return(result)

def solved(transited) :
    result = []
    for i in range(0,len(transited)) :
        result.append(0)
        result[i] = int(transited[i]) + 1
    print(sum(result))

if __name__ == '__main__' :
    word = input().strip()
    solved(transit(word))