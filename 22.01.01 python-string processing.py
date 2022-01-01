'''

문자열 처리 함수를 배워 보자.

1. lower => 특정 변수의 문장을 소문자로 바꿔서 출력해주는 함수
ex) print(변수이름.lower())

2. upper => 특정 변수의 문장을 대문자로 바꿔서 출력해주는 함수
ex) print(변수이름.upper())

3. islower => 특정 변수의 문장이 소문자인지 확인해서 소문자가 맞으면 True, 아니면 False 출력
ex) print(변수이름[~].islower())

4. isupper => 특정 변수의 문장이 대문자인지 확인해서 대문자가 맞으면 True, 아니면 False 출력
ex) print(변수이름[~].isupper())

5. len => 특정 변수의 문장의 길이가 몇인지 알려주는 함수.
ex) print(len(변수이름))

++
replace함수 => 변수 이름.replace => 변수에 들어있는 문자나 문자열을 다른 문자나 문자열로 바꿔주는 함수. 
ex) print(변수 이름.python("변수에 포함되어 있는 문자열", "바꾸고 싶은 문자열"))

find함수 -> 변수 이름.find => 변수의 문자열 중 원하는 문자가 어느 위치에 있는지 알려주는 함수
ex) print(변수 이름.find("변수에 들어있는 문자나 문자열"))

원하는 값이 없으면 -1를 출력하고 그 다음 문장을 이어서 출력.

index함수 -> 변수 이름.index => 변수의 문자열 중 원하는 문자가 어느 위치에 있는지 알려주는 함수 
ex)
index = 변수 이름.index("문자 / 문자열") 
print(index)

원하는 값이 없으면 그대로 출력을 멈춤.

count함수 -> 변수 이름.count =>변수의 문자열이나 문자가 몇 번 나오는지 알려주는 함수.
ex) print(변수 이름.count("변수에 들어있는 문자나 문자열:))

'''

team = "Dortmund is in Europe."

#team변수의 문자열을 모두 소문자로 바꾸기
print( team.lower() )

#team변수의 문자열을 모두 대문자로 바꾸기
print( team.upper() )

#team변수의 문자열이 소문자인지 물어보기
print( team[0].islower() )

#team변수의 문자열이 대문자인지 물어보기
print( team[0].isupper() )

#team변수의 문자열의 길이가 몇인지 출력하기
print(len(team))

#team변수의 문자열이 o를 몇 번 나오는지 출력하기
print(team.count("o"))

#team변수의 문자열의 o가 어느 위치에 있는지 출력하기-index함수 버전
index = team.index("o")
print(index)

index = team.index("o", index + 1)
print(index)

#team변수의 문자열의 o가 어느 위치에 있는지 출력하기-find함수 버전
print(team.find("Dortmund"))

print(team.find("note"))

print("hi")

#team변수의 문자열의 특정 문자를 다른 문자로 바꾸기

print(team.replace("Dortmund", "Ajax"))