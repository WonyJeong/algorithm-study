#가로 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열

area = int(input('넓이 입력 : '))

for i in range(1, area+1):
    if i*i > area : break
    if area % i : continue #continue문이 실행되면 루프 본문의 나머지 부분을 건너뛰고 조건식으로 돌아감
    print(f'{i} x {area // i }')