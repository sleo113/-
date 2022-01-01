# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# ex) https://naver.com

# 조건1 : https://는 제외하고 naver.com만 활용
# 조건2 : 처음 만나는 점(.) 이후 부분은 제외, 즉 naver만 활용.
# 조건3 : 남은 글자들 중 처름 세 자리 + 글자 갯수 + 글자 중 'e'의 갯수 + "!"로 구성해라 

# 예) 생성된 비밀번호 : nav51


#솔루션1
what = "naver"

print("nav{one}{two}!" .format(one = what.count("n")+what.count("a")+what.count("v")+what.count("e")+what.count("r") , two = what.count("e") ) )


#솔루션2

url = "https://naver.com"
my_str = url.replace("https://", "") #조건1

my_str = (my_str[0:5]) #조건2

print(my_str)

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)

print("{0}에서 당신의 비밀번호는 {1}입니다" .format(url, password))