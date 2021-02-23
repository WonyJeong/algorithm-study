#학생 5명의 시험점수를 입력받아 합계와 평균 출력

print('학생 그룹 점수의 합계와 평균을 구함')

score1 = int(input('1번 : '))
score2 = int(input('2번 : '))
score3 = int(input('3번 : '))
score4 = int(input('4번 : '))
score5 = int(input('5번 : '))

total = 0

total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점')
print(f'평균은 {total / 5}점')

#학생 수를 변경하는 경우 복잡
#특정 학생의 시험 점수를 확인하거나 변경하는 경우 복잡
# 최저점과 최고점을 구하거나 정렬이 필요한 경우 복잡