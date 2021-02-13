def solution(s):
    q, r = len(s) // 2, len(s) % 2
    return s[q+r-1:q+1]
