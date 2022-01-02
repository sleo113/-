'''

1. dictionary. 사전 배우기

key나 value 형태로 자료형이 나온다.

key는 중복이 안되며 key가 통하는 사물함만 열 수 있어야 한다.

사전은 정의할 떄 내용을 {}로 묶는다.

형태 => 
cabinet = {key라고 설정하는 값 : 내용(=value)}

1. print(cabinet[key에 해당하는 값])

2. print(cabinet.get(key에 해당하는 값))

ex) 
cabinet[ = {4 : "박떙떙"}
print(cabinet[[4])

cabinet[ = {4 : "박떙떙", 100 : "이떙떙"}
print(cabinet[[100])

만약

print(cabinet[key에 해당하는 값] 이때
key가 없으면 오류를 발생시키고 프로그램을 멈춤.

print(cabinet.get(key에 해당하는 값)) 이 때는
key가 없으면 None를 출력하고 그대로 다음 출력을 진행하며 프로그램을 지속한다.

또 만약 

print(cabinet.get(key에 해당하는 값)) 이 때
key에 해당하는 값에 정의하지 않은 것을 출력하고 싶다 그럼

ex) 
print(cabinet.get(key로 설정 되지 않은 값, "넣고 싶은 내용"))

사전 자료형 안에 특정 key값이 있는지 없는지 알고 싶다?

=> print(key값 in cabinet)이라고 하면 출력에 True나 False가 나온다.

2. 현재 cabinet에 새로운 걸 넣고 싶을 때

ex)
print(cabinet)
cabinet[key에 해당하는 값] = 새로 넣고 싶은 내용

만약 key에 해당하는 값이 원래 있었다면 새로 업데이트 되는 것임

3. key에 해당하는 값이 가지는 내용을 없애고 싶을때

del 즉, delete를 사용해 나타난다.

ex)
del cabinet[key에 해당하는 값]
print(cabinet)

4. 현재 총 사용하는 key들만 출력하고 싶을때

print(cabinet.keys())를 사용

5. 내용만 출력하려면

print(cabinet.values())를 사용

6. key들과 내용을 함께 출력하소 싶으면 

print(cabinet.items())를 사용

7. cabinet값을 모두 지우고 싶을때

cabinet.clear()를 사용

ex)
cabinet.clear()
print(cabinet)

'''
'''
cabinet = {4 : "박떙떙", 100 : "이떙떙"}
print(cabinet[4], cabinet[100])

print(cabinet.get(100))

print(cabinet.get(1, "임땡땡"))

print(4 in cabinet) #True

print(7 in cabinet) #False
'''

cabinet = {"A-7" : "박떙떙", "P-0" : "이떙떙"}
print(cabinet["A-7"], cabinet["P-0"])

print(cabinet)
cabinet["A-7"] = "사떙떙"
cabinet["P-1"] = "칠땡땡"
print(cabinet)

del cabinet["A-7"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)