#수식

print(2+4*5) #22

print( ( 2 + 7 ) * 9 ) #81 

number = 2 + 4 * 5 #22
print(number)

number = number + 9
print( number ) 

print( number / 8 )

number /= 2
print(number)

number = 22
number += 3 # 25
print(number)

number = 10
number -= 9
print(number)

#number를 number = 2 + 4 * 5를 고정으로 쓰려면 수식 전에 한 번 정의를 해줘야 한다.
#그러면 number 위에 number = 2 + 4 * 5 값인 22를 덮붙인 후 그 다음에 나오는 수식을 처리한다.

number = 10
number %= 9
print(number)

number = 10
print( number % 9 )

number = 10
number // 1
print(number)
# //는 print문에서 사용! 37행 읽히지도 못함...
