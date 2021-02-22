import sys
input = sys.stdin.readline

def reverse(N,sample_seq):
    for i in range(N) :
        if sample_seq[i] == 1:
            sample_seq[i] = 3
        elif sample_seq[i] == 2:
            sample_seq[i] = 4
        elif sample_seq[i] == 3 :
            sample_seq[i] = 1
        else :
            sample_seq[i] = 2

    sample_seq.reverse()
    return sample_seq
        


if __name__ == '__main__':
    N = int(input().strip())
    sample_seq = list(map(int, input().strip().split()))
    num = int(input().strip())
    suggested = [list(map(int, input().strip().split())) for _ in range(num)]

    sequences = []
    '''
    1. 주어진 표본 모양 수열로 만들 수 있는 정방향 수열 구하기
    '''
    for i in range(N):
        sequences.append(sample_seq[i:] + sample_seq[:i])

    '''
    2. 주어진 표본 모양 수열로 만들 수 있는 역방향 수열 구하기
    '''
    sample_seq = reverse(N,sample_seq)
    for i in range(N):
        sequences.append(sample_seq[i:] + sample_seq[:i])

    answer = []
    for suggest in suggested :
        for element in sequences :
            if suggest == element :
                answer.append(suggest)
                
    print(len(answer))
    for element in answer :
        for el in element :
            print(el, end=' ')
        print()