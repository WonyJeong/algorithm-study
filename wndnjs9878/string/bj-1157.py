#1157
import sys
input = sys.stdin.readline

def solved(alphabet):
    max = 0
    most = ''
    for i in range(65, 65+26) :
        if alphabet[i] > max : 
            max = alphabet[i]
            most = chr(i)
        elif alphabet[i] == max : 
            most = '?'
    print(most)

if __name__ == '__main__':
    usedAlphabet = []
    for i in range(0, 65+26) :
        usedAlphabet.append(0)
    word = input().strip().upper()
    for i in range(len(word)):
        usedAlphabet[ord(word[i])] += 1
    solved(usedAlphabet)