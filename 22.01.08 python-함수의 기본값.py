'''

0. 함수의 기본값을 설정하는 것을 배워보자.

공통되는 것이 있으면 기본값을 설정한다. 
어디에? 함수명 옆에 달려있는 ()안에

ex) proflie(age = 17)

++출력하려는 문장을 연결하려면 \를 사용하여 연결한다. 

ex) 
print(" 나는 진쩅쩅이고 \
    너는 종떙떙이다. ")
'''

# def profile(name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}\t" \
#         .format(name, age, main_lang))

# profile("구땡땡", 25,  "java")

def information(name, age = 18, team = "떙떙띵") :
    print("이름 : {0}\t 나이 : {1}\t 소속 팀 : {2}\t " \
        .format(name, age, team))

information("박떙떙")
information("궁떙떙")
information("지떙떙")