'''

파이썬에서 리스트를 배워보자.

#리스트 => list = []

ex)

train_list = ["박떙떙", "나떙떙", "구떙땡"]

리스트를 사용하여 여러 변수의 값을 하나의 변수의 값으로 바꿀 수 있다.

# 맨 뒤에 붙이는 함수.
append 함수 => 넣고 싶은 변수 이름.append(넣고 싶은 숫자/"문자/문자열")

ex)
train_list = ["박떙떙", "나떙떙", "구떙땡"]
train_list.append("자땡땡")
print(train_list)

# 어느 사이에 넣는 함수. 
insert 함수 => 넣고 싶은 변수 이름.insert(넣고 싶은 곳의 위치(0~), 넣고 싶은 숫자,"문자/문자열")

ex)
train_list = ["박떙떙", "나떙떙", "구떙땡"]
train_list.insert(0, "unifer)
print(train_list)

#뒤에서부터 하나씩 뺴기.
pop함수 => 변수이름.pop()

ex)
train_list = ["박떙떙", "나떙떙", "구떙땡"]
train_list.pop()
print(train_list)

#정렬 가능
sort함수 => 변수 이름.sort()

ex)
train_list = ["박떙떙", "나떙떙", "구떙땡"]
train_list.sort()
print(train_list)

#뒤집어버리는 함수
reserve함수 => 뒤집어서 나타내고 싶은 변수 이름.reverse()

ex)
train_list = ["박떙떙", "나떙떙", "구떙땡"]
train_list.reverse()
print(train_list)

#값 모두 지우기 함수
clear 함수 => 변수이름.cleaer()

ex)
train_list = ["박떙떙", "나떙떙", "구떙땡"]
train_list.clear()
print(train_list)

리스트는 자료형에 구애받지 않고 자유롭게 자료형을 여러가지 활용해서 사용 가능.
=> mix_list 활용
1. 변수 정의
ex) 
mun_list = [1, 2, 3]
mix_list = ["나때떙"]
print(mix_list)

#리스트 합치기
extend함수 활용 => 합치고 싶은 변수 이름1.extend(합치고 싶은 변수 이름2)

ex)

mun_list = [1, 2, 3]
mix_list = ["나때떙"]
mun_list.extend(mix_list)
print(mun_list)

'''

train_list = ["Harry", "Ryan", "Gorion"]
print(train_list) # ["Harry", "Ryan", "Gorion"]

train_list = ["Harry", "Ryan", "Gorion"]
train_list.append("Park")
print(train_list) # ["Harry", "Ryan", "Gorion", "append"]

train_list = ["Harry", "Ryan", "Gorion"]
train_list.insert(2, "Coco")
print(train_list) # ["Harry", "Ryan", "Coco", "Gorion"]

train_list = ["Harry", "Ryan", "Gorion"]
print(train_list) # ["Harry", "Ryan", "Gorion"]
train_list.pop()
print(train_list) # ["Harry", "Ryan"]
train_list.pop()
print(train_list) # ["Harry"]
train_list.pop()
print(train_list) # []

train_list = ["Harry", "Ryan", "Gorion"]
train_list.sort()
print(train_list) # ["Gorion" ,"Harry", "Ryan"]


train_list = ["Harry", "Ryan", "Gorion"]
train_list.reverse()
print(train_list) # ["Gorion", "Ryan", "Harry"]

train_list = ["Harry", "Ryan", "Gorion"]
train_list.clear()
print(train_list) # []

people_list = ["Harry", "Ryan", "Gorion"]
mix_list = [1, 2, 3,True]
people_list.extend(mix_list)
print(people_list) # ["Harry", "Ryan", "Gorion", 1, 2, 3, True]
