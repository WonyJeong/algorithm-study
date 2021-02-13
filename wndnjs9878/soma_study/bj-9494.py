#9494
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().strip())
    while N != 0 :
        text = []
        text.append(len(input().strip().split()[0]))
        result = text[0]
        for i in range(1,N):
            temp = input().strip()
            if len(temp) > text[i-1] :
                # print('추가되는 길이',len(temp[text[i-1]:].split()[0]) )
                # print('뭐추가돼?',temp[text[i-1]:].split()[0])
                if temp[text[i-1]] == ' ':
                    text.append(text[i-1])
                else :
                    text.append(text[i-1]+len(temp[text[i-1]:].split()[0]))
            else :
                text.append(text[i-1])

            if result < text[i]:
                result = text[i]
        # print(text)
        print(result+1)
        N = int(input().strip())