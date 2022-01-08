'''

0. 지역변수와 전역변수에 대해 배워보자.

1. 지역변수란 쉽게 말해 함수 내에서만 사용할 수 있는 것.
혹은 함수가 호출될 때 만들어졌다가 함수 호출이 끝나면 사라지는 것을 말한다.

2. 전역변수란 프로그램 내에서 어디서든 사용할 수 있는 함수이다.

global이란 라이브러리를 사용해서 함수 밖에 있는 변수의 값을 가져온다.

형태)

global 함수 밖에 있는 변수이름 

'''

# 송금 횟수 차감 및 제한하는 프로그램.
# 지역 변수를 사용한 버전 만들기
# 전역 변수를 사용한 버전 만들기
'''
def send_money(now, used) :
    time = 20 
    now = time - used
    print("현재 송금이 {0}회 가능 합니다. 송금하시겠습니까?" .format(time))
    print("횟수가 차감됩니다.")
    print("남은 송금 가능 횟수는 {0}회입니다." .format(now))

send_money(10, 2)
print(send_money)
'''

time = 10
tax = 100
money = 10000

# def send_money(now, used) :
#     now = time - used
#     if 0 <= used <= 10 :
#             print("현재 송금이 {0}회 가능 합니다. 송금하시겠습니까?" .format(time))
#             print("횟수가 차감됩니다.")
#             print("남은 송금 가능 횟수는 {0}회입니다." .format(now))
#             now -= 1
#     else :
#             print("수수료가 부과 됩니다.")
#             print("{0}원을 부과하시겠습니까?" .format(tax))
#             print("수수료가 부과됩니다.")
#             print("잔액 : {0}원" .format(money - tax))
#             return money - tax

# send_money(10 , 2)
# print(send_money)

def send_money(now, used) :
    global time
    now = time - used
    if 0 <= used <= 10 :
            print("현재 송금이 {0}회 가능 합니다. 송금하시겠습니까?" .format(time))
            print("횟수가 차감됩니다.")
            print("남은 송금 가능 횟수는 {0}회입니다." .format(now))
            now -= 1
    else :
            print("수수료가 부과 됩니다.")
            print("{0}원을 부과하시겠습니까?" .format(tax))
            print("수수료가 부과됩니다.")
            print("잔액 : {0}원" .format(money - tax))
            return money - tax

send_money(10 , 2)
print(send_money)