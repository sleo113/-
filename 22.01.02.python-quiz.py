'''

1. 파이썬 코딩 대회를 주최합니다.

2. 참석률을 높이기 위헤 댓글 이벤트를 진행하겠습니다.

3. 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 지급하겠습니다.

-조건에 맞게 추첨 프로그램을 작성하시오.-

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20이라고 가정.
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가.
조건3 : random 모듈과 shuffle, sample를 활용한다.

-출력 예제-
--당첨자 발표--
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하합니다--

-->shuffle함수 

shuffle(변수 이름)

shuffle => 섞어라!

-->sample함수

sample(변수 이름)

print(sample(변수 이름, 갯수) ) 

'''

from random import * 

people_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(people_list)
people_list = tuple(people_list)


print("--담첨을 축하합니다.--")
print( "치킨 당첨자 :", sample(people_list,1) )
print( "커피 당첨자 :", sample(people_list,3) )
print("--축하합니다!--")