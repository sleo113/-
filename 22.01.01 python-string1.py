from math import * 

day = 1+5

#print( day + sqrt(4) )

'''
print( day + sqrt(4) )에서 day를 str(day)로 바꾸면?
어떻게 되나?
'''

'''
print( str(day) + sqrt(4) )
하면 타입 오류가 나온다.

그럼 제곱근 함수에도 str를 붙이면?
'''

print( str(day) + str(sqrt(4)) )

'''
하면 62.0이 나온다.
why?

str = string을 의미?..

이 부분은 좀 더 파이썬을 배워보자.
'''