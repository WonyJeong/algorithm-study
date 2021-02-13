import sys
input = sys.stdin.readline
#2중포문 돌면 시간초과 -_-


if __name__ == '__main__':
    N = int(input().strip())
    mountaintop = list(map(int, input().strip().split()))
    maxtop = 0
    maxattack = 0
    for top in mountaintop :
        if top > maxtop :
            attack = 0
            maxtop = top
        else :
            attack += 1
        maxattack = max(maxattack, attack) # 지금까지의 최고봉을 저장해둠. 마지막 봉우리가 젤 높아버리면 attack이 0인채로 끝날테니까 그러면 이전까지의 가장 높은 attack이 답이 되어야 하므로
    
    print(maxattack)