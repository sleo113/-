'''

반복문을 배워 보자

=>for문
for 변수 정의 in [] :
    {
        print("내용 : {0}" .format(변수 이름))
    }

그냥 for문 
for 변수 이름 in 위에서 정의한 변수 :
    {
        print("변수 내용 {숫자}" .format(변수 이름))
    }


range 활용한 for문.

for 변수 이름 in range(숫자) :
    {
        print("변수 내용 {숫자}" .format(변수 이름))
    }

->범위 지정 가능
for 변수 이름 in range(시작, 끝 범위+1) :
    {
        print("변수 내용 {숫자}" .format(변수 이름))
    }

'''

for player_num in [0,1,2,3,4,5,6,7,8,9,10,11]:
    {
        print("선수 번호 ! : {0}" .format(player_num)) 
    } 
'''
선수 번혼 ! : 0
선수 번혼 ! : 1
선수 번혼 ! : 2
선수 번혼 ! : 3
선수 번혼 ! : 4
선수 번혼 ! : 5
선수 번혼 ! : 6
선수 번혼 ! : 7
선수 번혼 ! : 8 
선수 번혼 ! : 9 
선수 번혼 ! : 10
선수 번혼 ! : 11
'''

for player_num in range(1, 5):
    {
        print("선수 번호 ! : {0}" .format(player_num)) 
    } 

'''
선수 번혼 ! : 1
선수 번혼 ! : 2
선수 번혼 ! : 3
선수 번혼 ! : 4
'''