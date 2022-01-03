'''

1. 나는 cocoa 서비스를 이용하는 택시 기사님입니다
2. 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 :승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다 
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

-출력문 예제-
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 15분)

총 탑승 승객 : 2분
'''
'''

1. 난수 사용 위해 random 라이브러리 사용
2. 변수 이름 나열 customer
3. 반복문 활용 


'''

from random import *

for customer in range(1, 51) :
     time = randrange(5, 50)
     if 5 < time < 15 :
          print("[O] {0}번째 손님 (소요시간 : {1}(분)" .format(customer, time))
     else :
          print("[ ] {0}번째 손님 (소요시간 : {1}(분)" .format(customer, time))