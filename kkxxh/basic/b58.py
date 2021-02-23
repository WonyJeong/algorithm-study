#함수 내부 외부에서 정의한 변수와 객체의 식별 번호를 출력

n=1 
def put_id():
    x=1
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()

#1, n , x 식별번호가 모두 같다
