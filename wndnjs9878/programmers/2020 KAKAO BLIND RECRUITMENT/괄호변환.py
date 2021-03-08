import sys
input = sys.stdin.readline

def solution(p):
    u, v = [], []
    if correct(p): return p
    for i in range(2, len(p)+1,2):
        if balanced(p[:i]):
            u, v = p[:i], p[i:]
            break
    if correct(u): return u + solution(v)
    else:
        # print(u)
        # print(u[1:len(u)-1].replace('(','0').replace(')','(').replace('0',')'))
        return '(' + solution(v) + ')' + u[1:len(u)-1].replace('(','0').replace(')','(').replace('0',')')


def balanced(b): return b.count('(') == b.count(')')


def correct(c):
    cnt = 0
    for i in range(len(c)):
        cnt = cnt + 1 if c[i] == '(' else cnt - 1
        if cnt < 0: return False
    return True

if __name__ == '__main__':
    p = "()))((()" #균형잡힌 괄호 문자열 
    print(solution(p))