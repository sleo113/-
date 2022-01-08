'''

0. 키워드값을 이용한 함수 호출에 대해 배워보자.

키워드 값을 활용하면 순서가 섞여 있어도 
값을 각각 매개변수 값에 대입하여 출력할 수 있다

'''

def information(name, age, team ) :
    print(name, age, team)

information( team = "고고프로", age = 19, name = "박떙떙")
information(name = "궁떙떙", team = "레드", age = 20 )
information(age = 27 , name = "지떙떙", team = "블루")