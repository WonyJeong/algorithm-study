<h2 align = "center">
  알고리즘 스터디 진행을 위한 규칙
</h2>

## 우와 ! 2차 까지 끝났다!!    
약 한달 반동안 소마를 위해 열심히 준비한 모두를 위해 박수 ㅉㅉㅉ

## 우와 ! 2차 까지 다 붙어따!!! 무야호👐    
면접준비 ㅎㅇㅌ!

## 우와 ! 최종 까지 다 붙어따!!! 무야호👐    
이제 시작인가봅니다

## 소개
술먹다가 급발진을 하여 연이 된 널스케줄팀과 스터디 진행을 하게 되어 매우 반갑습니다
초면 무례한 행동은 잊어 주시고 알고리즘이나 하죠

## 스터디 진행 계획
제가 이전에 진행한 보편전인 알고리즘 스터디는 2~3일에 한번 각자 주제(DP, Greed Algorithm, 등)을 서로에게 소개시켜주며 개념과 백준의 유형문제를 소개하는 식으로 진행되었습니다.   
그러나 각자 귀찮을 것 같기도 하고 얼마 남지 않은 기간동안 많은 양의 알고리즘 공부를 진행하기 위해서 이 레포지토리를 생성하였습니다.    

이 레포지토리는 다음과 같은 구성을 갖추고자 합니다.  

>[root]      
>> [팀원 깃 아이디]  
>>> [알고리즘 분류]      
>>>> [백준문제번호.py]      

  각자의 폴더에 카카오 단톡방에서 정한 목표치를 정하여 문제를 풀고 자신의 디렉토리에 풀이한 문제를 업로드합니다.   
  또한 1일 1커밋(1문제 이상 풀이)는 확실히 하여 진행하면 좋을 것 같습니다. 지키지 못할 시 패널티를 정하는 것이 좋을 것 같아요.
  
  
  ## Rule's
  1. 레포지토리에 각 자신의 이름으로 된 폴더가 있고, 자신이 푼 알고리즘의 유형별로 문제를 정리한다.    
  2. 1일 1커밋 이상을 목표로 한다. 어길 시에 벌금 5천원을 술값으로 쓴다!   
  3. (제출할 자기소개서가 마무리 되기 전까지) 저녁(18시 ~ 19시)전까지는 알고리즘을 진행하고 이후 시간대에 자기소개서를 작성한다.    
  
  
  ## 꿀팁 (임시)
  
  * 입출력
  입출력을 위한 예제 코드입니다. 빠른 입출력을 위해 다음과 같이 사용한다 하니 알아두면 좋을 듯 해요.    
  아래 코드의 의미는 대략, 사용자의 입력을 input().strip() 을 이용하여 받고, 문자열 마지막의 띄어쓰기를 무시합니다.   
  그리고 .split()를 통해 띄어쓰기를 구분하고 map(int, ....) 를 이용하여 문자열을 int형으로 변환합니다.
 ``` python
   import sys 
   input = sys.stdin.readline
   
   M, N, K = map(int, input().strip().split())
   # 입력 예시 ) 1 2 3
   print(f'{M} {N} {K}') # 1 2 3 출력
 ```  
 
 * 알고리즘 코드 기본 틀은 다음과 같아요. ```if __name__ == "__main__":``` 는 c언어에서의 main 이라고 대강 생각하시면 됨니다잇
 > 이렇게 쓰는 이유는 네이버, 카카오, 소마 등 구름, 프로그래머스 기반의 코테 사이트들을 사용하는 코테는 함수형으로 알고리즘 문제를 짜야하기 때문입니다.
 > 그래서 `if __name__ == "__main__":` 아래에는 인풋 받는 부분과 main함수 하나만 작성하여 main함수에 인풋을 받아서 main 함수를 위쪽에 구현하는 방식으로 연습해봅시다.
 ``` python
  import sys
  input = sys.stdin.readline
  
  def myFunction(param):
    answer = []
    ...
    
    return answer[]

  if __name__ == "__main__":
      T = int(input().strip())
      for _ in range(0,T):
          ...
          myFunction([])
 ```
 
 
  * 강제종료
 ```python
  sys.exit(0)
  # sys.exit(1)하면 런타임에러 발생
 ```
 * [시간복잡도 계산](https://life-with-coding.tistory.com/273)
> 문제 풀기전에 자기 알고리즘 시간복잡도 대략이라도 계산해보고 코딩 시작하세요.
