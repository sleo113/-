'''

-함수에는 ()에 반환값이나 전달값을 넣을 수도 있고 안 넣을 수도 있다.

-함수에 반환값을 

ex) 

1. 
def open_account() :
    print("새로운 계좌가 생성되었습니다.")

open_account()

2. 입금
def open_account() :
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money) :
    print(" 입금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance + money))
    return balance + money
    
balance = 0
balance = deposit(balance, 1000)
print(balance)

3. 출금
def withdraw( balance, miner_money) :
    if balance == 0 or balance < 0 :
        print("출금을 하실 잔액이 없습니다." .format(balance))
    else :
        print("{0}원에서 {1}원을 출금합니다." .format(balance, miner_money)) 
    return balance - miner_money

balance = 10000
miner_money = 5000
balance = withdraw(balance, balance - miner_money)
print(balance)


'''

def open_account() :
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money) :
    print(" 입금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance + money))
    return balance + money

def withdraw( balance, miner_money) :
    if balance == 0 or balance < 0 :
        print("출금을 하실 잔액이 없습니다." .format(balance))    
    else :
        print("{0}원에서 {1}원을 출금합니다." .format(balance, miner_money)) 
        print("잔액은 {0}원입니다." .format(balance - miner_money))
        return balance - miner_money

balance = 10000
miner_money = 5000
balance = withdraw(balance, balance - miner_money)
print(balance)