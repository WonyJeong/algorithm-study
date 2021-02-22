#각 배열 원소의 최댓값을 구해서 출력

from b77 import max_of #b77.py의 max_of를 import

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.') #7
print(f'{s}의 최댓값은 {max_of(s)}입니다.') #t - 가장 큰 문자 코드
print(f'{a}의 최댓값은 {max_of(a)}입니다.') #FLAC - 사전 순으로 가장 큰 문자열