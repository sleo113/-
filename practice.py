# 1. 변수 1) 동물의 이름 2) 고유 이름 3) 나이 4) 취미?행동 
# 2. 불리안 설정-성체의 나이는 초기에 4로 설정
# 3. 다른 동물로 똑같이 프로그램 짜보기


animal = "사자"
name = "연탄이"
age = 3
hobby = "산책"
is_adult = age >= 4

print("우리 나라 동물원에는",animal +"이(가) 살고 있어요")
print("이름은", name+"이랍니다.")
print("나이는", str(age) + "살 입니다")
print("동물원에서 지내는",animal, name , "동물원에서" , "뭐하면서" , "지낼까요?")
print("바로!", hobby+"하면서 지낸답니다!")

print("이 쯤에서 퀴즈!", name + "이는", "성체일까요?")
print("답은!", str(age)+"이므로",  str(is_adult)+ "입니다!\n")

animal = "고릴라"
print("우리 나라 동물원에는",animal +"이(가) 살고 있어요")

name = " 꽝꽝이 "
print("이름은", name+"이랍니다.")

age = 5
print("나이는", str(age) + "살 입니다")

print("동물원에서 지내는", animal, name , "동물원에서" , "뭐하면서" , "지낼까요?")

hobby = "바나나 먹"
print("바로!", hobby+"으면서 지낸답니다!")

print("이 쯤에서 퀴즈!", name + "이는", "성체일까요?")

age = 5
is_adult = age > 3 
print("답은!", str(age)+"이므로",  str(is_adult)+ "입니다!")

