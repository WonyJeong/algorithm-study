#11947
import sys
input = sys.stdin.readline

def lovely(N):
    reversedN = ''
    for i in range(len(N)):
        reversedN += str(9 - int(N[i]))
    return int(N) * int(reversedN)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = input().strip()
        Max = 0
        if int(N)%10 == 0 : #100
            # print('10배수~~~~~')
            print(lovely(N))
        else : # int(N) < 10**(len(N)) : # 98 < 10^2
            #print('<')
            if int(N) <= (10**len(N))//2 : # 17 < 50
                print(lovely(N)) #17
            else : # 71
                print(lovely(str((10**len(N))//2))) # 50

