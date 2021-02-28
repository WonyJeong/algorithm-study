#1717
'''
1. parent를 자기 자신으로 초기화
2. 부모를 찾는 find함수
3. 합집합 연산 -> 같은 부모를 갖도록 union함수 제작
4. 연산을 입력받아 0이면 합집합 연산
                1이면 find를 통해 부모를 찾고 부모가 같으면 같은집합, 다르면 다른 집합에 포함되어있다
'''

import sys
input = sys.stdin.readline

def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    parent = [i for i in range(n+1)]

    for _ in range(m):
        flag, a, b = map(int, input().strip().split())
        if flag :
            if find(a) == find(b):
                print('YES')
            else :
                print('NO')
        else :
            union(a,b)


