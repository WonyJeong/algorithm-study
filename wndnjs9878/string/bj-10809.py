#10890
import sys
input = sys.stdin.readline

def alphabetInit(alphabet):
    for i in range(0,97+26) :
        alphabet.append(-1)
    return alphabet

def solved(alphabet) :
    for i in range(97, 97+26):
        print(alphabet[i], end=' ')

if __name__ == '__main__':
    alphabet = []
    alphabet = alphabetInit(alphabet)
    S = input().strip()
    for i in range(0,len(S)):
        if alphabet[ord(S[i])] != -1 : continue
        alphabet[ord(S[i])] = i
    
    solved(alphabet)
