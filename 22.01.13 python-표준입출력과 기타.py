'''

0. 표준 입출력에 대해 배워보자

sep와 end를 선언하는 것
end를 쓰면 한 줄로 나온다 또한 이 것의 의미는 문장의 끝부분을 원하는 것으로 바꿔달라는 뜻이다.

표준 입력 = input함수를 말한다.

표준 출력은 stdout으로 처리된다.
즉, 표준 출력으로 문장이 찍힌다.

stderr은 표준 에러로 처리된다.
이 경우 확인을 통해 코드를 수정해야 한다.

++
만약 어떤 것을 나열하는데 정렬하고 싶다면 
변수이름.ljust(숫자)와 변수이름.rjust(숫자)를 사용하면 된다
참고로 ljust는 왼쪽 정렬, rjust는 오른쪽 정렬을 말한다.

zfill()이란 것도 있다. 이것은 특정 자리 수만큼 공간을 확보하고 특정 수만큼
문자나 수를 넣은 뒤 나머지 부분은 모두 숫자 0응 넣는 것이다.

형태 : 변수이름.zfill(숫자)
'''

print("나는 누구입니다.", "나는 지금 웃고 있습니다.", \
    end = "나를 맞춰보세요!")
print("나는 누구일까요?")
# 이렇게 end를 문장 뒤에 사용하여 나타내면 문장의 끝에서 다음 문장을 실행한다.

print("나는 누구입니다.", "나는 지금 웃고 있습니다.", sep = ",")
# 이렇게 sep를 사용하면 ,나 +같이 출력문에서 연결할 수 있는 연산자 자리에 
# sep로 정의한 것이 들어간다.

answer = input("네가 좋아하는 아이스크림이 뭐야?")
print("제가 좋아하는 아이스크림은 {0}입니다.". format(answer))
# 표준 입력 함수는 input 함수다. 

# inmport sys를 선언하면 .file=sys.stdout과 file=sys.stderr를 사용할 수 있다.

import sys
print("python", "java", file=sys.stdout) # python java
print("python", "java", file=sys.stderr) # python java
'''
두 문장 모두 python java라고 출력이 된다.
이 둘은 별반 차이가 없는 것 같아 보이지만 
전자는 표준 출력으로 문장이 표시되고
후자는 표준 에러로 처리가 되는 것이다. 
이렇게 되면 전자는 표준 출력을 하는 것이므로 별 문제가 없는데
후자는 확인을 해서 코드를 바꾸어야 한다.

'''

#어떤 것을 나열할 때 정렬하기.
score = {"수학 " : 60, "과학 " : 80, "도덕 " : 90}
for subject, score in score.items():
    print(subject.ljust(7), str(score).rjust(5), sep=":")
# score는 숫자이므로 str처리를 하였고 ljust와 rjust의 ()안의 숫자는
# 총 몇 자리를 차지할지를 나타내는 것이다.

#zfill()사용해보기
for num in range(1, 21) :
    print("번호 순서 :" + str(num).zfill(4))
# 1~20까지 반복시키기 위해 반복문인 for문을 사용했고
# num변수는 숫자이기에 ste로 처리했으며 
#zfill()를 이용하여 특정 자리수 만큼을 설정했다.