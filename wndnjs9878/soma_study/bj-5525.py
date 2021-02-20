import sys
input = sys.stdin.readline

# BF
# def IOIOI(N,M,S):
#     for i in range(1,N+1):
#         Pn = 'IO' * i
#     Pn += 'I'
#     # print(Pn)
#     count = 0
#     for _ in range(S.find(Pn),M):
#         where = S.find(Pn)
#         # print(where)
#         if where != -1:
#             count += 1
#             S = list(S)
#             S[where] = 'O'
#             S = ''.join(S)
#             # print(S)
#     return count

def IOIOI(N,M,S):
    Pn = 0
    count = 0
    i = 1
    while i < M-1:
        if S[i-1]=='I' and S[i]=='O' and S[i+1]=='I':
            Pn += 1 #Pn에서 n의 값 체크
            if Pn == N:
                count += 1 
                Pn -= 1
            i += 1 #2. IOI가 있을 시엔 두 칸 옮김 IO건너뛰고 I부터 시작시키기 위함 
        else :
            Pn = 0
        i += 1 # 1. 무조건 한 칸 옮기는데
    return count

if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    S = input().strip()
    print(IOIOI(N,M,S))