'''
s[i:j] # s[i]부터 s[j-1]까지 나열
s[i:j:k] # s[i]부터 s[j-1]까지 k씩 건너뛰며 나열

i,j가 len(s)보다 크면 len(s)가 지정된 것으로 간주
인덱스와 달리 범위에서 벗어나는 값을 지정해도 오류가 발생하지 않음
i가 없거나 None이면 0이 지정된 것으로 간주
j가 없거나 None이면 len(S)가 지정된 것으로 간주

s[:] #리스트 s의 원소를 모두 출력
s[::-1] #리스트 s의 원소중 맨 끝에서부터 전부 출력

'''

s = [11,22,33,44,55,66,77]
print(s[0:6]) # [11,22,33,44,55,66]
print(s[0:7:2]) #[ 11,33,55,77]
print(s[-4:-2]) #[44,55] #뒤에서 4번째 원소부터 뒤에서 2번째 원소까지 출력
print(s[3:1]) #[] 오류 나지않음 

