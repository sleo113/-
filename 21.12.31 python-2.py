#파이썬이 제공하는 숫자 처리 함수!

# 1. abs함수
# 2. pow함수
# 3. max함수
# 4. min함수
# 5. round함수 
# 6. 매스 라이프러리=> from math import * 라고 정의하면 사용 가능
# 위에 꺼는 상관없음 밑에 꺼는 꼭 써야함. 안그러면 오류뜸
# { 
# floor함수 => 내림 함수
# ceil함수 =>올림 함수
# sqrt함수 =>제곱근 함수
# }

from math import *

print( floor(2.66) ) # 2 => 내림
print( round(2.66) ) # 3 => 반올림
print( ceil(2.66) ) # 3 => 올림
print( pow(2, 6) ) #64 => 거듭제곱 ======>64.0
#math 라이브러리는 수학에 관련된 함수임. 따라서 실수값으로 출력하기도 함.
print( max(3, 5) ) #5 => 최대값
print( min(2.99, 3) ) #2.99 => 최소값

print( abs(-9) + sqrt(4) ) #11 => 절대값, 제곱근
#수학 관련 함수들 끼리 더하는 거 가능 다른 연산들은?

print( abs(-9) - sqrt(4) ) #7

print( abs(-9) * sqrt(4) ) #

print( abs(-9) // sqrt(4) ) #4 

print( abs(-9) % sqrt(4) ) #1

print( abs(-9) / sqrt(4) ) #4.5